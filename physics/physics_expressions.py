
from imports import math

# =========================
# КИНЕМАТИКА
# =========================

def speed(distance: float, time: float) -> float:
    """Скорость: v = s / t (м/с)."""
    if time == 0:
        raise ValueError("Время не может быть равно нулю")
    return distance / time


def distance(speed: float, time: float) -> float:
    """Путь: s = v * t (м)."""
    return speed * time


def travel_time(distance: float, speed: float) -> float:
    """Время движения: t = s / v (с)."""
    if speed == 0:
        raise ValueError("Скорость не может быть равна нулю")
    return distance / speed


def acceleration(v0: float, v: float, time: float) -> float:
    """Ускорение: a = (v - v0) / t (м/с²)."""
    if time == 0:
        raise ValueError("Время не может быть равно нулю")
    return (v - v0) / time


def free_fall_time(height: float, g: float = 9.81) -> float:
    """Время свободного падения без сопротивления воздуха."""
    if height < 0 or g <= 0:
        raise ValueError("Высота должна быть >= 0, а g > 0")
    return math.sqrt(2 * height / g)


# =========================
# МЕХАНИКА
# =========================

def force(mass: float, acceleration: float) -> float:
    """Второй закон Ньютона: F = m * a (Н)."""
    return mass * acceleration


def weight(mass: float, g: float = 9.81) -> float:
    """Сила тяжести: F = m * g (Н)."""
    return mass * g


def momentum(mass: float, speed: float) -> float:
    """Импульс тела: p = m * v (кг·м/с)."""
    return mass * speed


def work(force: float, distance: float) -> float:
    """Работа постоянной силы вдоль движения: A = F * s (Дж)."""
    return force * distance


def kinetic_energy(mass: float, speed: float) -> float:
    """Кинетическая энергия: E = m * v² / 2 (Дж)."""
    return mass * speed ** 2 / 2


def potential_energy(
    mass: float,
    height: float,
    g: float = 9.81
) -> float:
    """Потенциальная энергия: E = m * g * h (Дж)."""
    return mass * g * height


def power(work_done: float, time: float) -> float:
    """Мощность: P = A / t (Вт)."""
    if time == 0:
        raise ValueError("Время не может быть равно нулю")
    return work_done / time


# =========================
# ДАВЛЕНИЕ И ПЛОТНОСТЬ
# =========================

def density(mass: float, volume: float) -> float:
    """Плотность: ρ = m / V (кг/м³)."""
    if volume == 0:
        raise ValueError("Объём не может быть равен нулю")
    return mass / volume


def pressure(force_value: float, area: float) -> float:
    """Давление: p = F / S (Па)."""
    if area == 0:
        raise ValueError("Площадь не может быть равна нулю")
    return force_value / area


def buoyant_force(
    density_liquid: float,
    volume: float,
    g: float = 9.81
) -> float:
    """Архимедова сила: F = ρ * g * V (Н)."""
    return density_liquid * g * volume


# =========================
# ТЕПЛОВЫЕ ЯВЛЕНИЯ
# =========================

def heat_quantity(
    mass: float,
    specific_heat: float,
    delta_temperature: float
) -> float:
    """Количество теплоты: Q = m * c * ΔT (Дж)."""
    return mass * specific_heat * delta_temperature


def kelvin_to_celsius(kelvin: float) -> float:
    """Перевод Кельвинов в градусы Цельсия."""
    return kelvin - 273.15


def celsius_to_kelvin(celsius: float) -> float:
    """Перевод градусов Цельсия в Кельвины."""
    return celsius + 273.15


# =========================
# ЭЛЕКТРИЧЕСТВО
# =========================

def ohm_voltage(current: float, resistance: float) -> float:
    """Закон Ома: U = I * R (В)."""
    return current * resistance


def ohm_current(voltage: float, resistance: float) -> float:
    """Закон Ома: I = U / R (А)."""
    if resistance == 0:
        raise ValueError("Сопротивление не может быть равно нулю")
    return voltage / resistance


def ohm_resistance(voltage: float, current: float) -> float:
    """Закон Ома: R = U / I (Ом)."""
    if current == 0:
        raise ValueError("Ток не может быть равен нулю")
    return voltage / current


def electric_power(voltage: float, current: float) -> float:
    """Электрическая мощность: P = U * I (Вт)."""
    return voltage * current


def electric_charge(current: float, time: float) -> float:
    """Электрический заряд: q = I * t (Кл)."""
    return current * time


# =========================
# КОЛЕБАНИЯ И ВОЛНЫ
# =========================

def frequency(period: float) -> float:
    """Частота: f = 1 / T (Гц)."""
    if period == 0:
        raise ValueError("Период не может быть равен нулю")
    return 1 / period


def wave_speed(wavelength: float, frequency_value: float) -> float:
    """Скорость волны: v = λ * f (м/с)."""
    return wavelength * frequency_value
