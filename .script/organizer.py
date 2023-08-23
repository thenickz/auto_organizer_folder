# code
import os


formats = {
    'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.ico', '.webp', '.jp2', '.raw', 'avif'],
    'instaladores': ['.exe', '.msi'],
    'office': {
        'sheets':['.xls', '.xlsx', '.ods'],
        'ppts':['.ppt', '.pptx', '.odp'],
        'texts':['.doc', '.docx', '.odt']
    },
    'pdf': ['.pdf'],
    'programas': ['.py', '.cpp', '.java', '.sh', '.c', '.h', '.rb', '.php', '.html', '.css', '.js', '.swift', '.go', '.lua', '.pl', '.r', '.sql', '.scala', '.vb', '.ts', '.dart', '.kt', '.rs', '.asm', '.m', '.json', '.xml', '.yaml', '.ini', '.toml', '.coffee', '.scss', '.sass', '.less', '.jsx', '.tsx', '.vue', '.ejs', '.php', '.asp', '.jsp', '.as', '.bat', '.ps1', '.vbs', '.ahk', '.lisp', '.perl', '.f90', '.matlab', '.cobol', '.haskell', '.fortran', '.groovy', '.erlang', '.d', '.elixir', '.clojure', '.rust', '.ada', '.powershell', '.sql', '.tcl', '.smalltalk', '.scheme', '.forth', '.verilog', '.f#', '.pawn', '.abap', '.awk', '.prolog', '.dart', '.haxe', '.objectpascal', '.postscript', '.qml', '.racket', '.rexx', '.sas', '.scilab', '.simula', '.sparql', '.vala', '.vhdl', '.x10', '.zshell'],
    'zip': ['.zip', '.rar', '.7z']
}

path = r'C:\Users\nicolas\Desktop\auto_organizer_folder\Downloads'
with os.scandir(path) as scan:
    files = [item.name for item in scan if item.is_file()]


if files:
    for item in files:
        file_name, file_extension = os.path.splitext(item)
        new_file_name = file_name.lower().replace(" ", "_") + file_extension
        
        # Verifique as extensões nos formatos definidos
        for category, extensions in formats.items():
            if file_extension.lower() in extensions:
                # Mova o arquivo para a pasta correspondente com o novo nome
                source_path = os.path.join(path, item)
                destination_path = os.path.join(path, category, new_file_name)
                os.makedirs(os.path.join(path, category), exist_ok=True)  # Cria a pasta se não existir
                os.rename(source_path, destination_path)
                break  # Parar de verificar outras categorias após encontrar uma correspondência
        else:
            # Nenhuma correspondência encontrada, mover para a pasta 'outros'
            other_folder = os.path.join(path, 'outros')
            os.makedirs(other_folder, exist_ok=True)
            destination_path = os.path.join(other_folder, new_file_name)
            os.rename(os.path.join(path, item), destination_path)
