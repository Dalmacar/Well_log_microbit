import serial
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

PORT = "/dev/tty.usbmodem1421202"   # your micro:bit port
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
print(f"Connected to {PORT}")

depths = []
gr_values = []

TRACK_TITLE = "Real-Time GR Log"
CURVE_NAME = "GR"
X_LABEL = "Gamma Ray (API)"
Y_LABEL = "Coordinate"
LINE_COLOR = "black"
LINE_WIDTH = 2.0

# Lithology colors
CARBONATE_COLOR = "#4A90E2"   # blue
SAND_COLOR = "#F4D03F"        # yellow
SHALE_COLOR = "#03652C"       # green

# Lithology patterns
CARBONATE_HATCH = "||"   # carbonate / limestone-like
SAND_HATCH = ".."        # sand dots
SHALE_HATCH = "---"      # shale lines

# GR cutoffs
CARBONATE_MAX = 10
SAND_MAX = 30

plt.ion()
fig, ax = plt.subplots(figsize=(4, 8))

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    if not line:
        continue

    print("Received:", line)

    # Fix input format: [0,10] -> 0,10
    line = line.replace("[", "").replace("]", "")

    parts = line.split(",")
    if len(parts) != 2:
        continue

    try:
        depth = float(parts[0])   # coordinate from car
        gr = float(parts[1])      # GR value
    except ValueError:
        continue

    if len(depths) == 0 or depth != depths[-1]:
        depths.append(depth)
        gr_values.append(gr)

    ax.clear()

    # Fill lithology intervals
    if len(depths) >= 2:
        for i in range(len(depths) - 1):
            y1 = depths[i]
            y2 = depths[i + 1]
            x = gr_values[i]

            if x <= CARBONATE_MAX:
                fill_color = CARBONATE_COLOR
                hatch_style = CARBONATE_HATCH
            elif CARBONATE_MAX < x <= SAND_MAX:
                fill_color = SAND_COLOR
                hatch_style = SAND_HATCH
            elif x > SAND_MAX:
                fill_color = SHALE_COLOR
                hatch_style = SHALE_HATCH
            else:
                continue   # leave 30 to 90 unfilled

            ax.fill_betweenx(
                [y1, y2],
                0,
                x,
                facecolor=fill_color,
                edgecolor="black",
                hatch=hatch_style,
                linewidth=0.6,
                alpha=0.8
            )

    # Original GR log style
    ax.step(
        gr_values,
        depths,
        where="post",
        color=LINE_COLOR,
        linewidth=LINE_WIDTH,
        label=CURVE_NAME
    )

    ax.set_title(TRACK_TITLE, fontsize=14, fontweight="bold")
    ax.set_xlabel(X_LABEL, fontsize=12, fontweight="bold")
    ax.set_ylabel(Y_LABEL, fontsize=12, fontweight="bold")

    # Well-log style: depth/coordinate increases downward
    ax.invert_yaxis()

    # Typical GR scale
    ax.set_xlim(0, 150)

    ax.grid(True, linestyle="--", alpha=0.5)

    legend_handles = [
        Patch(facecolor=CARBONATE_COLOR, edgecolor="black", hatch=CARBONATE_HATCH, label="Carbonate"),
        Patch(facecolor=SAND_COLOR, edgecolor="black", hatch=SAND_HATCH, label="Sand"),
        Patch(facecolor=SHALE_COLOR, edgecolor="black", hatch=SHALE_HATCH, label="Shale"),
    ]
    ax.legend(handles=legend_handles, loc="upper right")

    plt.tight_layout()
    plt.pause(0.01)