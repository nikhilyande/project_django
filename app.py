import qrcode
from flask import Flask, render_template, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.form.get('full_name')
        location = request.form.get('location')
        phone_number = request.form.get('phone_number')
        age = request.form.get('age')
        password = request.form.get('password')

        # Generate QR code
        qr_data = f"Full Name: {full_name}\nLocation: {location}\nPhone Number: {phone_number}\nAge: {age}"
        qr_code = qrcode.make(qr_data)

        # Save QR code to a BytesIO object
        qr_io = BytesIO()
        qr_code.save(qr_io)
        qr_io.seek(0)

        # Clear form data
        full_name = ""
        location = ""
        phone_number = ""
        age = ""
        password = ""

        # Return QR code image
        return send_file(qr_io, mimetype='image/png')

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)