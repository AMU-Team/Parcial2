Feature: Gestión de reinos
  Los jugadores pueden crear, actualizar y eliminar sus reinos en el juego.

  Scenario: Crear un nuevo reino
    Given El jugador está conectado al juego
    When El jugador ingresa el nombre "Reino del Norte" y confirma
    Then EL "Reino del Norte" debe aparecer en la lista

  Scenario: Actualizar un reino existente
    Given El reino "Reino del Norte" esta en la lista de reinos
    When El jugador cambia el nombre a "Reino del Sol" y confirma
    Then El "Reino del Sur" debe actualizarse a "Reino del Sol"

  Scenario: Eliminar un reino
    Given El reino "Reino del Norte" esta en la lista de reinos
    When El jugador eliminar el reino y confirma
    Then El "Reino del Este" debe eliminarse de la lista
