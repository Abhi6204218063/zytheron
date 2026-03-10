from openmm.app import *
from openmm import *
import openmm.unit as unit


def run_md():

    pdb = PDBFile("receptor_fixed.pdb")

    forcefield = ForceField("amber14-all.xml")

    system = forcefield.createSystem(pdb.topology)

    integrator = LangevinIntegrator(
        300 * unit.kelvin, 1 / unit.picosecond, 0.002 * unit.picoseconds
    )

    try:
        platform = Platform.getPlatformByName("CUDA")
    except:
        platform = Platform.getPlatformByName("CPU")

    simulation = Simulation(pdb.topology, system, integrator, platform)

    simulation.context.setPositions(pdb.positions)

    simulation.minimizeEnergy()

    simulation.step(500)

    state = simulation.context.getState(getEnergy=True)

    return state.getPotentialEnergy()
