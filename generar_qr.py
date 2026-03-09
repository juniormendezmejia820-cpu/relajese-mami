import qrcode
enlace = "https://juniormendezmejia820-cpu.github.io/relajesemami/"
imagen_qr = qrcode.make(enlace)
imagen_qr.save("QR_Vuala_Oficial.png")
print("¡Listo! El QR se guardó en esta carpeta.")