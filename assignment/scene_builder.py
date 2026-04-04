"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
roof_width = 6
roof_depth = 4
roof_y_position = 4
roof_x = -8
roof_z = 5


roof = cmds.polyCube(
   name="roof",
   width=roof_width,
   height=roof_depth,
   subdivisionsX=1,
   subdivisionsY=1,
)[0]
# Creates roof shape.
cmds.rotate(90, 0, 0)
cmds.move(roof_x, building_height, roof_z, roof)
# moves roof on top of building.
# ---------------------------------------------------------------------------
# TODO: Add Object 3
# ---------------------------------------------------------------------------
sun_radius = 8
sun_y_position = 8
sun_x = 8
sun_z = 8

sun = cmds.polySphere(
   name="sun",
   radius=sun_radius,
   subdivisionsX=1,
   subdivisionsY=1,
)[0]
# Creates sun shape.
cmds.move(0, 14, -14, sun)
# Moves sun up and backwards.
cmds.scale (0.25, 0.25, 0.25)
# Shrinks sun down by 0.25.
# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------
trunk_radius = 2
trunk_height = 6
trunk_depth = 4
trunk_x = 8
trunk_z = -5


trunk = cmds.polyCylinder(
   name="trunk",
   radius=trunk_radius,
   height=trunk_depth,
   subdivisionsX=1,
   subdivisionsY=1,
)[0]
# Creates trunk shape.
cmds.scale (0.2, 1, 0.2)
# Scales trunk to be thinner.
cmds.move (trunk_x, building_height /3, trunk_z, trunk)
# moves trunk in the opposite end of the building and roof, and makes sure it is aligned with the floor.
# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------
leaves_radius = 2
leaves_y_position = 2
leaves_x = 8
leaves_z = -5

leaves = cmds.polySphere(
   name="leaves",
   radius=leaves_radius,
   subdivisionsX=1,
   subdivisionsY=1,
)[0]
# Creates leaves shape.
cmds.move (leaves_x, trunk_height /2, leaves_z, leaves)
# Moves leaves to be on top of the trunk.
# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
