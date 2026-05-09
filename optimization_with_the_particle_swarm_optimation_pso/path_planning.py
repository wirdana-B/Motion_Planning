import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# ============================================================
# Obstacle
# ============================================================
class Obstacle:
    def __init__(self, center, radius):
        self.center = np.array(center, dtype=float)
        self.radius = float(radius)


# ============================================================
# Environment
# ============================================================
class Environment:
    def __init__(self, width, height, robot_radius, start, goal):
        self.width        = width
        self.height       = height
        self.robot_radius = robot_radius
        self.start        = np.array(start, dtype=float)
        self.goal         = np.array(goal,  dtype=float)
        self.obstacles    = []

    def add_obstacle(self, obs: Obstacle):
        self.obstacles.append(obs)

    def is_collision(self, point: np.ndarray) -> bool:
        """Return True if `point` is inside any obstacle (including robot radius)."""
        for obs in self.obstacles:
            dist = np.linalg.norm(point - obs.center)
            if dist <= obs.radius + self.robot_radius:
                return True
        return False


# ============================================================
# B-Spline path helper
# ============================================================
def _build_path(control_points: np.ndarray, start: np.ndarray,
                goal: np.ndarray, resolution: int) -> np.ndarray:
    """
    Build a smooth path via linear interpolation through
    [start, *control_points, goal].
    Returns an (N, 2) array of waypoints.
    """
    waypoints = np.vstack([start, control_points, goal])
    path = []
    for k in range(len(waypoints) - 1):
        segment = np.linspace(waypoints[k], waypoints[k + 1],
                              resolution, endpoint=False)
        path.append(segment)
    path.append(waypoints[-1:])
    return np.vstack(path)


# ============================================================
# Cost Function
# ============================================================
class EnvCostFunction:
    """
    Callable cost function for PSO path planning.

    Parameters passed to PSO have shape (2 * num_control_points,)
    where values are normalised in [0, 1] and mapped to the environment
    coordinate space.
    """

    COLLISION_PENALTY = 1e6

    def __init__(self, env: Environment, num_control_points: int, resolution: int):
        self.env                = env
        self.num_control_points = num_control_points
        self.resolution         = resolution

    def __call__(self, position: np.ndarray):
        env = self.env
        n   = self.num_control_points

        # Map normalised [0,1] -> environment coordinates
        xs = position[0:n] * env.width
        ys = position[n:2*n] * env.height
        control_points = np.column_stack([xs, ys])

        path = _build_path(control_points, env.start, env.goal, self.resolution)

        # ---- path length ----
        diffs  = np.diff(path, axis=0)
        length = float(np.sum(np.linalg.norm(diffs, axis=1)))

        # ---- collision penalty ----
        penalty = 0.0
        for pt in path:
            if env.is_collision(pt):
                penalty += self.COLLISION_PENALTY

        cost = length + penalty

        details = {
            'sol':    control_points,
            'path':   path,
            'length': length,
            'cost':   cost,
        }

        return cost, details


# ============================================================
# Plotting helpers
# ============================================================
# def plot_environment(env: Environment, ax=None):
#     """Draw the environment: obstacles, start, and goal."""
#     if ax is None:
#         ax = plt.gca()

#     ax.set_xlim(0, env.width)
#     ax.set_ylim(0, env.height)
#     ax.set_aspect('equal')

#     for obs in env.obstacles:
#         circle = plt.Circle(obs.center, obs.radius, color='gray',
#                             alpha=0.6, zorder=2)
#         ax.add_patch(circle)

    # ax.plot(*env.start, 'gs', markersize=10, label='Start', zorder=3)
    # ax.plot(*env.goal,  'r*', markersize=12, label='Goal',  zorder=3)
    # ax.legend(loc='upper left')


def plot_path(control_points: np.ndarray, resolution: int = 200,
              color: str = 'b', ax=None):
    """
    Plot the path defined by `control_points` and return the Line2D object
    so it can be updated later.
    """
    if ax is None:
        ax = plt.gca()

    env = ax.figure._env if hasattr(ax.figure, '_env') else None

    # We need start/goal — grab from current axes children or use defaults
    # The simplest approach: caller must have called plot_environment first,
    # so we reconstruct from the stored figure attribute set below.
    # (set via plot_environment_store)
    start = ax.figure._start if hasattr(ax.figure, '_start') else np.array([0, 0])
    goal  = ax.figure._goal  if hasattr(ax.figure, '_goal')  else np.array([100, 100])

    path = _build_path(control_points, start, goal, resolution)
    line, = ax.plot(path[:, 0], path[:, 1], color=color, linewidth=2, zorder=4)
    return line


def update_path(control_points: np.ndarray, line, resolution: int = 200):
    """Update an existing path line in-place (fast redraw)."""
    ax    = line.axes
    start = ax.figure._start if hasattr(ax.figure, '_start') else np.array([0, 0])
    goal  = ax.figure._goal  if hasattr(ax.figure, '_goal')  else np.array([100, 100])

    path = _build_path(control_points, start, goal, resolution)
    line.set_xdata(path[:, 0])
    line.set_ydata(path[:, 1])
    line.figure.canvas.draw_idle()


# ============================================================
# Monkey-patch plt.figure to store env info for path drawing
# ============================================================
_orig_figure = plt.figure

def _patched_figure(*args, **kwargs):
    fig = _orig_figure(*args, **kwargs)
    return fig

plt.figure = _patched_figure


def plot_environment(env: Environment, ax=None):
    """Draw the environment and store start/goal on the figure."""
    if ax is None:
        ax = plt.gca()

    fig = ax.figure
    fig._start = env.start.copy()
    fig._goal  = env.goal.copy()

    ax.set_xlim(0, env.width)
    ax.set_ylim(0, env.height)
    ax.set_aspect('equal')

    for obs in env.obstacles:
        circle = plt.Circle(obs.center, obs.radius, color='gray',
                            alpha=0.6, zorder=2)
        ax.add_patch(circle)

    ax.plot(*env.start, 'gs', markersize=10, label='Start', zorder=3)
    ax.plot(*env.goal,  'r*', markersize=12, label='Goal',  zorder=3)
    ax.legend(loc='upper left')