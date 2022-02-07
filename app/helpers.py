import uuid


def convert_to_slug(title):
    """
    Fungsi untuk mengubah judul menjadi slug(alamat untuk mengakses post)
    judul post akan dipisahkan dengan strip dan digabungkan dengan 
    angka yang acak menghasilkan sebuah alamat yang unik 
    """
    # title separated by dash, and id ex: this-is-title-1628349812219
    # slug operations
    # replace space on title with dash
    # add uuidv1 and generate the hex version
    return str(title.replace(' ', '-') + '-' + str(uuid.uuid4().int))


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jfif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
