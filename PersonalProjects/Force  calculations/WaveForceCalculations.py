# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:00:09 2022

@author: cresp
"""

import pandas as pd
import numpy as np
import math


#LIMITATIONS

#The Morison equation is a heuristic formulation of the force fluctuations in an oscillatory flow. 
#The first assumption is that the flow acceleration is more-or-less uniform at the location of the body.
# For instance, for a vertical cylinder in surface gravity waves this requires that the diameter of the cylinder
# is much smaller than the wavelength. If the diameter of the body is not small compared to the wavelength, 
#diffraction effects have to be taken into account.

# Second, it is assumed that the asymptotic forms: the inertia and drag force contributions, valid for very small
#  and very large Keulegan–Carpenter numbers respectively, can just be added to describe the force 
#  fluctuations at intermediate Keulegan–Carpenter numbers. However, from experiments it is found that in thi
#  s intermediate regime—where both drag and inertia are giving significant contributions—the Morison equation
#  is not capable of describing the force history very well. Although the inertia and drag coefficients can be
#  tuned to give the correct extreme values of the force.

# Third, when extended to orbital flow which is a case of non uni-directional flow, for instance encountered by a 
# horizontal cylinder under waves, the Morison equation does not give a good representation of the forces as a function 
# of time.

#SUPPORT FUNCTIONS

def mm3_to_m3(V):
    return V/(10**9)

def mm2_to_m2(S):
    return S/(10**6)

def volume_cyl_calc(radius, height):
    return PI*(radius**2)*height

def volume_cavecyl_calc(big_radius,small_radius, height):
    return PI*((big_radius**2)-(small_radius**2))*height

def mass_calc(volume, density):
    return volume*density

def archimede(density,volume):
    return density*volume*g

def lateral_surface_cylinder_calc(radius, height):
    return 2*PI*height*radius

def knots_to_ms(k):
    return k*0.514444

def drag_lateral_force(density,rel_speed,drag_c,area,wave_amp):
    return 0.5*density*(rel_speed**2)*drag_c*area*(wave_amp/2)

def froude_krylov_force(density, area, wave_amp):  #simple formula, like F = A*p
    return area*density*g*(wave_amp/2)

#DATA SECTION

PI = math.pi
g = 9.81
base_radius = 500 #mm
leg_radius = 125 #mm
big_base_height = 500 #mm
small_base_height = 400 #mm
leg_height = 600 #mm
lenght_outside_buoy = 150 #mm
water_density = 1000 #kg/m*3 - tap water density
steel_density = 8000 #kg/m*3 - AlSi 316 Stainless Steel

# DATA ABOUT THE THICKNESSES
base_thickness = 10 #mm
wall_thickness = 5 #mm
leg_int_thickness=5 #mm
water_level = 190 #mm
base_internal_radius = base_radius-wall_thickness
big_base_wall_height = big_base_height-(2*base_thickness)
leg_internal_radius = leg_radius - wall_thickness
small_base_wall_height = small_base_height-(2*base_thickness)
height_outside_water = 150 #mm - measured from the top of the big base to the water level (in average)
height_wall_outside_water = height_outside_water-base_thickness


#ASSUMPTIONS

#Neglection of air mass in the calculation of the weight

#VOLUME UPPER BASE [m3]

v_plate_base = mm3_to_m3(volume_cyl_calc(base_radius,base_thickness)) #m3
v_wall_big_base = mm3_to_m3(volume_cavecyl_calc(base_radius,base_internal_radius,big_base_wall_height)) #height of 500 mm
v_total_big_base = 2*v_plate_base+v_wall_big_base # sum of the 2 cylindrical platform and wall base

#VOLUME LOWER BASE[m3]

v_wall_small_base = mm3_to_m3(volume_cavecyl_calc(base_radius,base_internal_radius,small_base_wall_height)) #height of 400 mm
v_total_small_base = 2*v_plate_base+v_wall_small_base # sum of the 2 cylindrical platform and wall base

#VOLUME LEG [m3]

v_wall_leg = mm3_to_m3(volume_cavecyl_calc(leg_radius,leg_internal_radius,leg_height))  #600 mm of leg height


#BUOY VOLUME [m3]

V_BUOY = v_total_big_base + v_total_small_base + v_wall_leg

#INSIDE WATER VOLUME [m3]

v_water = mm3_to_m3(volume_cyl_calc(base_internal_radius,water_level))

#BUOY MASS  [kg]

m_buoy = mass_calc(V_BUOY,steel_density)
m_water = mass_calc(v_water,water_density)
total_mass_buoy = m_buoy + m_water # 

#BUOY MASS OUSIDE WATER [kg]

v_wall_outside_water = mm3_to_m3(volume_cavecyl_calc(base_radius,base_internal_radius,height_wall_outside_water))
v_buoy_outside_water =  v_plate_base + v_wall_outside_water
mass_buoy_outside_water = mass_calc(v_buoy_outside_water,steel_density)

#BUOY MASS IN WATER  [kg]

v_buoy_in_water = V_BUOY-v_buoy_outside_water+v_water
v_buoy_in_water_nowaterinside = V_BUOY-v_buoy_outside_water
mass_buoy_in_water = total_mass_buoy-mass_buoy_outside_water

# TOTAL BUOY VOLUME IMMERSED IN WATER

big_base_volume_in_water = mm3_to_m3(volume_cyl_calc(base_radius, (big_base_height-height_outside_water)))
leg_volume_in_water = mm3_to_m3(volume_cyl_calc(leg_radius, leg_height))
small_base_volume_in_water = mm3_to_m3(volume_cyl_calc(base_radius, small_base_height))
v_total_buoy_in_water = big_base_volume_in_water+leg_volume_in_water+small_base_volume_in_water

#########################################################################################################################

#ASSUMPTIONS

#The surfaces that are pushed by water current is half total body immersed surfaces

#Due to cylindrical shapes, internal bases of cylinders are neglected, in according to Kim 2021 (in the documentation)


water_speed_min =knots_to_ms(0) #[m/s] - 0.76 knots - taken from measurements from Port of Rotterdam Dashboard from 27th July to 24th August
water_speed_max = knots_to_ms(2.5) #[m/s] - 1,46 knots - taken from measurements from Port of Rotterdam Dashboard from 27th July to 24th August
water_speed_average = knots_to_ms(1.25) #[m/s]
C_drag = 1.20 #(according to Cao2014)
max_height_of_tide = 2300 #mm from 0 to max


#   WEIGHT FORCE CALCULATION [N]

weight_force_all_buoy = total_mass_buoy*g
weight_force_buoy_in_water = mass_buoy_in_water*g
weight_force_buoy_outside_water = mass_buoy_outside_water*g

#  ARCHIMEDE FORCE

arch_f = archimede(water_density,v_total_buoy_in_water)

# SURFACE CALCULATIONS [M2]

big_base_immersed_surface = mm2_to_m2(lateral_surface_cylinder_calc(base_radius,big_base_height-height_outside_water)/2)
leg_immersed_surface = mm2_to_m2(lateral_surface_cylinder_calc(leg_radius,leg_height)/2)
small_base_immersed_surface = mm2_to_m2(lateral_surface_cylinder_calc(base_radius,small_base_height)/2)

# VISCOSITY EFFECT - DRAG FORCE, MORRISON EQUATION


F_drag_big_base = drag_lateral_force(water_density, water_speed_average, C_drag, big_base_immersed_surface,max_height_of_tide/1000)
F_drag_leg = drag_lateral_force(water_density, water_speed_average, C_drag, leg_immersed_surface,max_height_of_tide/1000)
F_drag_small_base = drag_lateral_force(water_density, water_speed_average, C_drag, small_base_immersed_surface,max_height_of_tide/1000)


# FROUDE - KRYLOV FORCE

F_froude_krylov_big_base = froude_krylov_force(water_density,big_base_immersed_surface,max_height_of_tide/1000)
F_froude_krylov_leg = froude_krylov_force(water_density,leg_immersed_surface,max_height_of_tide/1000)
F_froude_krylov_small_base = froude_krylov_force(water_density,small_base_immersed_surface,max_height_of_tide/1000)

# TOTAL LATERAL FORCE

lateral_forces_big_base = F_drag_big_base + F_froude_krylov_big_base
lateral_forces_leg = F_drag_leg + F_froude_krylov_leg
lateral_forces_small_base = F_drag_small_base + F_froude_krylov_small_base

var = dir()