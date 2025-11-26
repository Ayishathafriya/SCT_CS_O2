from PIL import Image
import numpy as np

def encrypt_image(image_path, key=123, method='xor'):
    img = Image.open(image_path)
    img_array = np.array(img)

    if method == 'xor':
        encrypted_array = img_array ^ key  # XOR each pixel with key
    elif method == 'add':
        encrypted_array = (img_array + key) % 256  # Add key and wrap around
    elif method == 'swap':
        encrypted_array = img_array[::-1, ::-1]  # Reverse rows and columns
    else:
        raise ValueError("Unsupported method")

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    return encrypted_img

def decrypt_image(encrypted_img, key=123, method='xor'):
    encrypted_array = np.array(encrypted_img)

    if method == 'xor':
        decrypted_array = encrypted_array ^ key
    elif method == 'add':
        decrypted_array = (encrypted_array - key) % 256
    elif method == 'swap':
        decrypted_array = encrypted_array[::-1, ::-1]
    else:
        raise ValueError("Unsupported method")

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    return decrypted_img
