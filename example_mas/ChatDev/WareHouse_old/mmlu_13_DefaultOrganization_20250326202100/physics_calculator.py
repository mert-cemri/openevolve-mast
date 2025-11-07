'''
This file contains the PhysicsCalculator class which provides methods to calculate uncertainties in physics problems.
'''
class PhysicsCalculator:
    @staticmethod
    def calculate_kinetic_energy_uncertainty(speed_uncertainty):
        '''
        Calculate the uncertainty in kinetic energy given the uncertainty in speed.
        Kinetic energy (KE) is proportional to the square of the speed (v^2).
        Therefore, the percentage uncertainty in KE is twice the percentage uncertainty in speed.
        :param speed_uncertainty: The percentage uncertainty in speed.
        :return: The percentage uncertainty in kinetic energy.
        '''
        return 2 * speed_uncertainty