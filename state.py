from telebot.asyncio_handler_backends import State, StatesGroup
from enum import Enum

class Convert2State(StatesGroup):
    filename = State()    # Menerima file .txt
    name = State()        # Nama file vcf pertama
    cname = State()       # Nama kontak per file
    totalc = State()      # Jumlah kontak per file
    totalf = State()      # Jumlah file
    file_change_count = State()  # Berapa kali berganti nama file
    file_change_frequency = State()  # Setiap berapa file nama file akan berganti
    file_names = State()  # Nama file yang akan digunakan saat perubahan nama

class ConvertXlsImagesState(State):
    filename = State()
    name = State()

class ConvertState(StatesGroup):
    filename = State()
    name = State()
    cname = State()
    totalc = State()
    totalf = State()

class ConvertVcfState(StatesGroup):
    filename = State()
    name = State()
    cname = State()
    totalc = State()
    totalf = State()

class ConvertXlsxState(StatesGroup):
    filename = State()
    name = State()

class PecahTxtState(StatesGroup):
    filename = State()
    name = State()
    totaln = State()
    totalf = State()

class PecahVcfState(StatesGroup):
    filename = State()
    name = State()
    totalc = State()
    totalf = State()

class ConvertVcfToTxtState(StatesGroup):
    filename = State()
    name = State()

class GabungVcfState(StatesGroup):
    waiting_for_files = State()  
    name = State()

class ChatToTxtState(StatesGroup):
    waiting_for_text_input = State()

class WiFiWpsWpaState(StatesGroup):
    waiting_for_interface = State()  # User input interface
    waiting_for_bssid = State()  # User input BSSID
    waiting_for_channel = State()  # User input channel

class GabungTxtState(StatesGroup):
    waiting_for_files = State()  # Menunggu pengguna mengunggah file
    name = State() 
    
class HapusSpasiState(StatesGroup):
    waiting_for_file = State()

class VipState(StatesGroup):
  user_id = State()
  durasi = State()

class kolomState(StatesGroup):
    waiting_for_file = State()

class HitungCtcState(StatesGroup):
    waiting_for_files = State()  # State where the bot is waiting for .vcf files

