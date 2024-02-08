from PIL import Image, ImageDraw, ImageFont
import os
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

def generate_certificate_and_send_email(name, mark, output_path='C:\\Desktop\\Python 100 days\\quiz\\certi'):
    with open("email.txt", "r") as file:
                emails = file.read()

    # Assuming 'arial.ttf' is in the current working directory, adjust the path if needed
    font_path = os.path.join(os.getcwd(), 'arial.ttf')
    font = ImageFont.truetype(font_path, 60)

    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    
    # draw.text(xy=(900, 695), text='{}'.format(name), fill=(0, 0, 0), font=font)
    draw.text(xy=(700, 695), text='Name: {}'.format(name), fill=(0, 0, 0), font=font)
    draw.text(xy=(1000, 695), text='  and  Score: {}%'.format(mark), fill=(0, 0, 0), font=font)


    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Save the certificate with a unique name
    certificate_filename = '{}_certificate.jpg'.format(name)
    certificate_path = os.path.join(output_path, certificate_filename)
    img.save(certificate_path)

    # Store in MySQL database
    try:
        con = pymysql.connect(host="localhost", user='root', password='2845', database='userdata')
        mycursor = con.cursor()

        # Assuming you have a table named 'certificates' with columns 'name' and 'file_path'
        query = 'INSERT INTO userdata (file_path) VALUES (%s) where email=(%s)'
        mycursor.execute(query, (certificate_path, emails))
        con.commit()
        
    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()

    # Send email with the certificate as an attachment
    sender_email = 'dharmkasundra284@gmail.com'
    sender_password = 'bkxs ghob fhxn vmtj'
    
    subject = 'Certificate for {}'.format(name)
    body = 'Dear {},\n\nAttached is your certificate.\n\nRegards,\nYour Organization'.format(name)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = emails
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(certificate_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= {}".format(certificate_filename))
    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, emails, msg.as_string())

    # Delete the file from the folder after storing in the database and sending email
    

