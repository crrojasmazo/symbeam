from symbeam.beam import beam

print("\n ============================================================================= ")
print(" Debuggin script for Symbeam")
print(" ============================================================================= ")

test_beam = beam('l', x0=0)
test_beam.add_support(0, 'pin')
test_beam.add_support('l', 'pin')
test_beam.add_distributed_load(0, 'l/2', '2 * q / l * x')
test_beam.add_distributed_load('l/2', 'l', 'q')
test_beam.check_beam_properties()
