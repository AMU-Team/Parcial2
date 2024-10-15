Feature: Gestión de recursos
  Los jugadores pueden recolectar y gestionar recursos dentro de su reino para el desarrollo y la expansión.

  Scenario: Recolectar recursos
    Given El reino "soldeoro" tiene una producción establecida
    When El reino "soldeoro" recolecta recursos
    Then Sus recursos de oro y madera crecen

  Scenario: Construir infraestructura
    Given El reino "soldeoro" tiene suficiente oro y madera para la construccion
    When El reino "soloro" construye una infraestructura "Granja"
    Then La "Granja" se añade al reino "sol de oro" y sus recursos decrecen según el costo

  Scenario: Expandir territorio
    Given El reino "soldeoro" tiene suficiente oro y madera para la expansión
    When El reino "soldeoro" expande su territorio
    Then Sus territorios debe incrementarse y sus recursos decrecen según el costo
