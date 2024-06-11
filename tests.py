import pytest
from datetime import datetime, timedelta
from src.timelog import Timelog

import os
import sys

# Função para configurar dinamicamente o PYTHONPATH
def configure_pythonpath():
    # Obtém o caminho do diretório atual do script de teste
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Obtém o caminho do diretório 'src' em relação ao diretório do script de teste
    src_dir = os.path.join(current_dir, '..', 'src')

    # Adiciona o diretório 'src' ao PYTHONPATH se não estiver lá
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

# Configura o PYTHONPATH antes de importar os módulos do 'src'
configure_pythonpath()

@pytest.fixture
def timelog():
    return Timelog()

def test_start_and_end_work(timelog):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=8)
    timelog.start_work(start_time)
    timelog.end_work(end_time)
    assert timelog.get_worked_hours() == timedelta(hours=8)

def test_start_and_end_pause(timelog):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=1)
    timelog.start_pause(start_time)
    timelog.end_pause(end_time)
    assert timelog.get_paused_hours() == timedelta(hours=1)

def test_worked_hours_with_no_start_or_end_time(timelog):
    assert timelog.get_worked_hours() == 0

def test_paused_hours_with_no_start_or_end_time(timelog):
    assert timelog.get_paused_hours() == 0