from django.db import models

class ClinicaFilteredManager(models.Manager):
    """Manager personalizado para filtrar dados por clínica do usuário logado"""
    
    def for_clinica(self, clinica):
        """Retorna queryset filtrado pela clínica especificada"""
        return self.filter(clinica=clinica)
    
    def for_user_clinica(self, user):
        """Retorna queryset filtrado pela clínica do usuário"""
        if user.clinica:
            return self.filter(clinica=user.clinica)
        return self.none()

class PacienteManager(ClinicaFilteredManager):
    """Manager específico para Paciente"""
    pass

class AgendamentoManager(ClinicaFilteredManager):
    """Manager específico para Agendamento"""
    
    def for_professor(self, professor):
        """Retorna agendamentos do professor na sua clínica"""
        return self.filter(medico=professor, clinica=professor.clinica)
    
    def for_aluno(self, aluno):
        """Retorna agendamentos do aluno na sua clínica"""
        return self.filter(aluno=aluno, clinica=aluno.clinica)

class ProntuarioManager(ClinicaFilteredManager):
    """Manager específico para Prontuario"""
    
    def for_professor(self, professor):
        """Retorna prontuários do professor na sua clínica"""
        return self.filter(professor=professor, clinica=professor.clinica)
    
    def for_coordenador(self, coordenador):
        """Retorna prontuários do coordenador na sua clínica"""
        return self.filter(clinica=coordenador.clinica)

