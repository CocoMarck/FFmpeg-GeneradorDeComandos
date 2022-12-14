'''Modulo de prueba para usar en mis programas jejej'''

import os, platform

def System():
    sys = platform.system()
    if sys == 'Windows': sys = 'win'
    elif sys == 'Linux': sys = 'linux'
    else: sys = 'linux'
    return sys

sys = System()

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

def CleanScreen(sys=sys):
    '''Limpiar pantalla'''
    if sys == 'linux':
        os.system('clear')
    elif sys == 'win':
        os.system('cls')
    else: pass

def Separator(spc = 128, smb = '#', see = True, sys=sys):
    '''Separar texto'''
    txt = smb*spc
    if see == True:
        print(txt)
    elif see == False:
        txt += '\n'
    else:
        pass
    return txt

def Continue(txt='¿Continuar?', lang = 'español', msg = False, sys=sys):
    idm = ['']*2
    if lang == 'español': idm[0], idm[1] = 's', 'n'
    elif lang == 'english': idm[0], idm[1] = 'y', 'n'
    else: idm[0], idm[1] = '', ''

    if msg == False:
        opc = input(f'{txt} {idm[0]}/{idm[1]}: ')
        if opc == 's': CleanScreen(sys)
        elif opc == 'n': CleanScreen(sys)
        elif opc == '':
            print('No escribiste nada')
            opc = Continue(txt=txt, lang=lang)
        else: 
            print(f'"{opc}" No existe')
            opc = Continue(txt=txt, lang=lang)
    else:
        opc = ''
        input(f'La opcion "{txt}" no existe\n'
              'Precione enter para continuar...')
        
    return opc

def Name(txt = 'Archivo', sys=sys):
    nme = input(Title(txt=f'Nombre de {txt}', see=False) +
              'Nombre: ')
    if nme == '':
        nme ='No_name'
    else: pass
    CleanScreen(sys)
    return nme

def Path(txt = 'Ruta', sys=sys):
#    pth = ''
    CleanScreen(sys)
    pth_fin = ''
    opc = input(Title(txt=txt, see=False) +
        "¿Elegir ruta? s/n: ")
    if sys == 'linux':
        pth_fin = '/'

        if opc == "s":
            pth = input("Escribe la ruta: ")
        else: pth = "$HOME/"

    elif sys == 'win':
        pth_fin = '\\'

        if opc == "s":
            pth = input("Escribe la ruta: ")
        else:
            pth = (os.path.join(os.path.join(os.environ['USERPROFILE']),
                   'Desktop'))

    else: pth = ''

    if pth == '':
        if sys == 'win':
            pth = (os.path.join(os.path.join(os.environ['USERPROFILE']),
                   'Desktop'))
        elif sys == 'linux': pth = '$HOME/'
        else: pass

    try: pth_laststr = pth[-1]
    except: pth_laststr = pth_fin
    if pth_laststr == pth_fin: pass
    else:        
        pth = pth + pth_fin

    CleanScreen(sys)
    return pth

def FFmpeg(opc = 'Help', txt='', flt=2, see = True, sys=sys):
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
        try:
            rsl_h = int(input('Ancho: '))
            rsl_v = int(input('Alto: '))
        except:
            rsl_h, rsl_v = 854, 480
            input('Tienes que escribir numereos enteros\n'
                  f'La resolución sera {rsl_h}x{rsl_v}\n'
                  'Preciona enter para continuar...')
        CleanScreen(sys)
#        rsl = f'-s {rsl_h}x{rsl_v}'
        cfg = f'-s {rsl_h}x{rsl_v}'

    elif opc == 'Quality':
        if see == True:
            if txt == '': Title(txt='Calidad')
            else: Title(txt=txt)
        else: pass

        print("Rango de 0-50. Donde 0 es la mejor calidad y 50 la peor.\n")

        try: crf = int(input('CRF: '))
        except:
            crf = 51
            print('Tienes que escribir nuemeros enteros.')

        if crf <= 50:
            cfg = f'-crf {crf}'
        else:
            cfg = '-crf 23'
            opc = Continue("Fuera de rango (de 0 a 50)\n"
                          f"El CRF sera {cfg}.\n¿Continuar?", sys=sys)
            if opc == 's': pass
            else: cfg = ''
        CleanScreen(sys)

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

        try: fps = int(input('Fotogramas: '))
        except:
            fps = 20
            input('Tienes que escribir numeros enteros\n'
                  f'Los fps seran {fps}\n'
                  'Preciona enter para continuar...')

        cfg = f'-r {fps}'
        CleanScreen(sys)

    elif opc == 'Preset':
        if see == True:
            if txt == '': Title(txt='Uso de CPU')
            else: Title(txt=txt)
        else: pass

        try:
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
        except:
            pst = 0
            print('Tienes que escribir numeros enteros.')

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
                            "¿Continuar?", sys=sys)
            if opc == 's': pass
            else: cfg = ''
        cfg = pst
        CleanScreen(sys)

    elif opc == 'Audio':
        if see == True:
            if txt == '': Title(txt='Audio')
            else: Title(txt=txt)
        else: pass

        print("#Seleccione un numero\n"
            "#EJEMPLO\n"
            "#    Audio: 1\n")
        if sys == 'linux':
            os.system('pactl list short sources')
            adi = input('\nAudio: ')
            cfg = f"-f pulse -i {adi}"
        elif sys == 'win':
            os.system('ffmpeg -list_devices true -f dshow -i dummy')
            adi = input('\nAudio: ')
            cfg = f'-f dshow -i audio="{adi}"'
        else: cfg = ''

        CleanScreen(sys)

    elif opc == 'AudioFilter':
        adi = [''] * flt
        nmr = flt
        txt = ''
        cfg = ''
        if flt > 0:        
            opc = Continue(f'La cantidad de audios a grabar son {flt}\n'
                            "¿Continuar?", sys=sys)
            if opc == 's': pass
            else: nmr, flt = 0, 0

            if sys == 'linux':
                while flt > 0:
                    adi[flt - 1] = FFmpeg('Audio', f'Audio {flt}',
                                          sys='linux')
                    flt = flt - 1
            elif sys == 'win':
                while flt > 0:
                    adi[flt - 1] = FFmpeg('Audio', f'Audio {flt}',
                                          sys='win')
                    flt = flt - 1
            else: cfg = ''

        else:
            CleanScreen(sys)
            input(f'"{flt}" Significa que no quieres grabar audio.\n'
                  'Preciona enter para continuar...')
            cfg = ''
            CleanScreen(sys)

        while nmr > 0:
            txt = adi[nmr - 1] + ' ' + txt
            cfg = txt
            #input(f"{adi[nmr - 1]}"), <- Para mostrar las fuentes de audio
            nmr = nmr - 1

    else: cfg = '#Error'

    return cfg