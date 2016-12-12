[Mesh]
  type = FileMesh
  file = singlefiber.e
  dim = 2
[]

[Variables]
  [./u]
  [../]
[]

[Kernels]
  [./HeatConductioneq]
    type = HeatConduction
    variable = u
  [../]
  [./linearheatgen]
    type = BodyForce
    variable = u
    value = 182.3 # W/cm
    block = 1
  [../]
[]

[BCs]
  [./outside]
    type = DirichletBC
    variable = u
    boundary = 1
    value = 800 # K
  [../]
[]

[Materials]
  [./fiber]
    type = HeatConductionMaterial
    block = 1
    thermal_conductivity = .2 # W/cmK
  [../]
  [./sicblock]
    type = HeatConductionMaterial
    block = 2
    thermal_conductivity = .08 # W/cmK
  [../]
[]

[Executioner]
  # Preconditioned JFNK (default)
  type = Steady
  solve_type = PJFNK
  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre boomeramg'
[]

[Outputs]
  exodus = true
[]

