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
# Added Roof shape.
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
# Added sun shape.
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
# Created trunk shape.
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
# Added leaves shape
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

# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
