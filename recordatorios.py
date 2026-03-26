def generar_recordatorio(paciente, fecha, hora):
    if not paciente or not fecha or not hora:
        return "Error: datos incompletos"
    return f"Recordatorio para {paciente}: cita médica el {fecha} a las {hora}"
