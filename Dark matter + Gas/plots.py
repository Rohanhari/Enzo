import yt

ds = yt.load('RD0011/RedshiftOutput0011')

sc = yt.create_scene(ds, lens_type='perspective')

# Get a reference to the VolumeSource associated with this scene
# It is the first source associated with the scene, so we can refer to it
# using index 0.
source = sc[0]

# Set the bounds of the transfer function
source.tfh.set_bounds((3e-31, 5e-27))

# set that the transfer function should be evaluated in log space
source.tfh.set_log(True)

# Make underdense regions appear opaque
source.tfh.grey_opacity = True

# Plot the transfer function, along with the CDF of the density field to
# see how the transfer function corresponds to structure in the CDF
source.tfh.plot('transfer_function.png', profile_field='density')

# save the image, flooring especially bright pixels for better contrast
sc.save('rendering.png', sigma_clip=6.0)
