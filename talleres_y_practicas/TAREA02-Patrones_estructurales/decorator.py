#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#* ejemplo obtenido desde el canal de youtube BettaTech: https://www.youtube.com/watch?v=Ab9HxiPLryg
#*--------------------------------------------------

# COMPONENTE
class Enemy():
    def take_damage(self) -> float:
        pass

    def movement_speed(self) -> float:
        pass

# Componente concreto enemigo base
class BaseEnemy(Enemy):
    def take_damage(self) -> float:
        return 10

    def movement_speed(self) -> float:
        return 10

# Componente enemigo invencible (enemigo que no recibe daño)
class InvencibleEnemy(Enemy):
    def take_damage(self) -> float:
        return 0

    def movement_speed(self):
        return 0

# Clase decorator
class EnemyDecorator(Enemy):
    _enemy: Enemy = None

    def __init__(self, enemy: Enemy) -> None:
        self._enemy = enemy

    @property
    def enemy(self) -> Enemy:
        return self._enemy

    def take_damage(self) -> float:
        return self._enemy.take_damage()

    def movement_speed(self) -> float:
        return self._enemy.movement_speed()

# Concrete decorators
class HelmetDecorator(EnemyDecorator):
    def take_damage(self) -> float:
        return self.enemy.take_damage() * 0.5

# Concrete decorators
class BootsDecorator(EnemyDecorator):
    def take_damage(self) -> float:
        return self._enemy.take_damage() * 0.2

    def movement_speed(self) -> float:
        return self._enemy.movement_speed() * 2

if __name__ == "__main__":
    # Crear un enemigo base
    base_enemy = BaseEnemy()
    print(f"Damage dealt to base enemy: ", base_enemy.take_damage())
    print(f"Movement speed of the base enemy: ", enemy_with_helmet.movement_speed())
    print()

    # Le agrega un casco al enemigo
    enemy_with_helmet = HelmetDecorator(base_enemy)
    print(f"Damage dealt to the enemy with helmet: ", enemy_with_helmet.take_damage())
    print(f"Movement speed of the enemy with helmet and boots: ", enemy_with_helmet.movement_speed())
    print()

    # Le agrega botas al enemigo
    enemy_with_boots_helmet = BootsDecorator(enemy_with_helmet)
    print(f"Damage dealt to the enemy with boots and helmet: ", enemy_with_boots_helmet.take_damage())
    print(f"Movement speed of the enemy with helmet and boots: ", enemy_with_boots_helmet.movement_speed())
