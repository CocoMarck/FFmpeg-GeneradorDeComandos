'''Modulo de prueba para usar en mis programas jejej'''

import os

def Title(txt = '', smb = '#', see = True, spc = 4):
    '''Mostrar un titulo'''
    spc = ' '*spc
    txt = f'{smb}{spc}{txt}{spc}{smb}'
    if see == True:
        print(txt)
    elif see == False:
        txt += '\n'
    else:
        pass
    return txt

def CleanScreen(opc = 'linux'):
    '''Limpiar pantalla'''
    if opc == 'linux':
        os.system('clear')
    elif opc == 'win':
        os.system('cls')
    else:
        pass

def Separator(spc = 128, smb = '#', see = True):
    '''Separar texto'''
    txt = smb*spc
    if see == True:
        print(txt)
    elif see == False:
        txt += '\n'
    else:
        pass
    return txt

def Continue(txt='¿Continuar?', lang = 'español'):
    idm = ['']*2
    if lang == 'español': idm[0], idm[1] = 's', 'n'
    elif lang == 'english': idm[0], idm[1] = 'y', 'n'
    else: idm[0], idm[1] = '', ''

    opc = input(f'{txt} {idm[0]}/{idm[1]}: ')
    if opc == 's': CleanScreen()
    elif opc == 'n': CleanScreen()
    else: pass
    return opc

def Name(txt = 'Archivo'):
    nme = input(Title(txt=f'Nombre de {txt}', see=False) +
              'Nombre: ')
    CleanScreen()
    return nme

def Path():
#    pth = ''
    CleanScreen()
    opc = input(Title(txt='Ruta', see=False) +
        "¿Elegir ruta? s/n: ")
    if opc == "s":
        pth = input("$HOME/")
        pth = f"$HOME/'{pth}'"
    else:
        pth = "$HOME/"

    CleanScreen()
    return pth

def FFmpeg_Resolution(txt = ''):
    print(Title(txt=f'Resolucion de {txt}', see=False) +
        Title(txt='(ancho X alto)', see=False) +
        "#EJEMPLOS\n"
        "#1920x1080\n"
        "#1280x720\n"
        "#854x480\n")
    rsl_h = int(input('Ancho: '))
    rsl_v = int(input('Alto: '))
    CleanScreen()
    rsl = f'-s {rsl_h}x{rsl_v}'
    return rsl

def FFmpeg_Quality(txt = 'Calidad'):
    print(Title(txt = txt, see = False) +
        "Rango de 0-50. Donde 0 es la mejor calidad y 50 la peor.\n")
    crf = int(input('CRF: '))
    if crf <= 50:
        crf = f'-crf {crf}'
    else:
        crf = '-crf 23'
        print(f"Fuera de rango (de 0 a 50)\n"
            f"El CRF sera {crf}.\n")
        Continue()
    CleanScreen()
    return crf

def FFmpeg_Frame():
    print(Title(txt='Fotogramas deseados', see=False) +
        Title(txt='(fotogramas X segundo)', see=False) +
        "#EJEMPLOS\n"
        "15\n"
        "30\n"
        "60\n")
    fps = int(input('Fotogramas: '))
    fps = f'-r {fps}'
    CleanScreen()
    return fps

def FFmpeg_Preset():
    pst = int(input(Title(txt='Uso de CPU', see = False) +
        "#PRESETS:\n"
        "#Rango del 1 al 9. Donde 1 es la opcion que usa "
        "menos cpu y 9 la que usa mas cpu.\n"
        "1.ultrafast\n"
        "2.superfast\n"
        "3.veryfast\n"
        "4.faster\n"
        "5.fast\n"
        "6.medium\n"
        "7.slow\n"
        "8.slower\n"
        "9.veryslow\n"
        'Preset: '))

    if pst == 1: pst = '-preset ultrafast'
    elif pst == 2: pst = '-preset superfast'
    elif pst == 3: pst = '-preset veryfast'
    elif pst == 4: pst = '-preset faster'
    elif pst == 5: pst = '-preset fast'
    elif pst == 6: pst = '-preset medium'
    elif pst == 7: pst = '-preset slow'
    elif pst == 8: pst = '-preset slower'
    elif pst == 9: pst = '-preset veryslow'
    else:
        pst = '-preset medium'
        print(f"Esa opcion no existe.\nEl preset sera {pst}.\n")
        Continue()
    CleanScreen()
    return pst

def FFmpeg_Audio(txt = 'Dispositivos de audio'):
    print(Title(txt = txt, see = False) +
        "#Seleccione un numero\n"
        "#EJEMPLO\n"
        "#    Audio: 1\n")
    os.system('pactl list short sources')
    adi = input('\nAudio: ')
    adi = f"-f pulse -i {adi}"
    CleanScreen()
    return adi

def FFmpeg_AudioFilter(flt = 2):
    adi = [''] * flt
    nmr = flt
    txt = ''
    if flt >= 1:        
        Continue(txt = f'¿La cantidad de audios a grabar son {flt}?')
        while flt > 0:
            adi[flt - 1] = FFmpeg_Audio(txt = f'Dispositivo numero {flt}')
            flt = flt - 1        
    else:
        CleanScreen()
        input(f'"{flt}" Significa que no quieres grabar audio.')
        main()

    while nmr > 0:
        txt = adi[nmr - 1] + ' ' + txt
        #input(f"{adi[nmr - 1]}"), <- Para mostrar las fuentes de audio
        nmr = nmr - 1
    return txt



def FFmpeg(opc = 'Help', txt='', flt=2, see = True):
    if opc == 'Help':
        if see == True:
            if txt == '': Title(txt='Ayuda')
            else: Title(txt=txt)
        else: pass
        os.system('ffmpeg -help')

    elif opc == 'Resolution':
        if see == True:
            if txt == '': Title(txt='Resolucion de Entrada')
            else: Title(txt=txt)
        else: pass

        print(Title('(ancho X alto)', see=False) +
            "#EJEMPLOS\n"
            "#1920x1080\n"
            "#1280x720\n"
            "#854x480\n")
        rsl_h = int(input('Ancho: '))
        rsl_v = int(input('Alto: '))
        CleanScreen()
#        rsl = f'-s {rsl_h}x{rsl_v}'
        cfg = f'-s {rsl_h}x{rsl_v}'

    elif opc == 'Quality':
        if see == True:
            if txt == '': Title(txt='Calidad')
            else: Title(txt=txt)
        else: pass

        print("Rango de 0-50. Donde 0 es la mejor calidad y 50 la peor.\n")
        crf = int(input('CRF: '))
        if crf <= 50:
            cfg = f'-crf {crf}'
        else:
            cfg = '-crf 23'
            opc = Continue("Fuera de rango (de 0 a 50)\n"
                          f"El CRF sera {crf}.\n¿Continuar?")
            if opc == 's': pass
            else: cfg = ''
        CleanScreen()

    elif opc == 'Frame':
        if see == True:
            if txt == '': Title(txt='Fotogramas desados')
            else: Title(txt=txt)
        else: pass

        print(Title('(fotogramas X segundo)', see=False) +
            "#EJEMPLOS\n"
            "#15\n"
            "#30\n"
            "#60\n")
        fps = int(input('Fotogramas: '))
        cfg = f'-r {fps}'
        CleanScreen()

    elif opc == 'Preset':
        if see == True:
            if txt == '': Title(txt='Uso de CPU')
            else: Title(txt=txt)
        else: pass

        pst = int(input("#PRESETS:\n"
            "#Rango del 1 al 9. Donde 1 es la opcion que usa "
            "menos cpu y 9 la que usa mas cpu.\n"
            "1.ultrafast\n"
            "2.superfast\n"
            "3.veryfast\n"
            "4.faster\n"
            "5.fast\n"
            "6.medium\n"
            "7.slow\n"
            "8.slower\n"
            "9.veryslow\n"
            'Preset: '))

        if pst == 1: pst = '-preset ultrafast'
        elif pst == 2: pst = '-preset superfast'
        elif pst == 3: pst = '-preset veryfast'
        elif pst == 4: pst = '-preset faster'
        elif pst == 5: pst = '-preset fast'
        elif pst == 6: pst = '-preset medium'
        elif pst == 7: pst = '-preset slow'
        elif pst == 8: pst = '-preset slower'
        elif pst == 9: pst = '-preset veryslow'
        else:
            pst = '-preset medium'
            opc = Continue(f"Esa opcion no existe.\nEl preset sera {pst}.\n"
                            "¿Continuar?")
            if opc == 's': pass
            else: cfg = ''
            Continue()
        cfg = pst
        CleanScreen()

    elif opc == 'Audio':
        if see == True:
            if txt == '': Title(txt='Audio')
            else: Title(txt=txt)
        else: pass

        print("#Seleccione un numero\n"
            "#EJEMPLO\n"
            "#    Audio: 1\n")
        os.system('pactl list short sources')
        adi = input('\nAudio: ')
        cfg = f"-f pulse -i {adi}"
        CleanScreen()

    elif opc == 'AudioFilter':
        adi = [''] * flt
        nmr = flt
        txt = ''
        cfg = ''
        if flt >= 1:        
            opc = Continue(f'La cantidad de audios a grabar son {flt}\n'
                            "¿Continuar?")
            if opc == 's': pass
            else: nmr, flt = 0, 0

            while flt > 0:
                adi[flt - 1] = FFmpeg(opc='Audio')
                flt = flt - 1        
        else:
            CleanScreen()
            input(f'"{flt}" Significa que no quieres grabar audio.')
            main()

        while nmr > 0:
            txt = adi[nmr - 1] + ' ' + txt
            cfg = txt
            #input(f"{adi[nmr - 1]}"), <- Para mostrar las fuentes de audio
            nmr = nmr - 1

    else: cfg = 'Opcion inexistente'

    return cfg