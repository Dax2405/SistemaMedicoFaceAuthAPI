import face_recognition
import numpy as np


def encode_face(image_bytes: bytes):
    image = face_recognition.load_image_file(image_bytes)
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        return face_encodings[0]
    return None


def compare_faces(known_encoding, unknown_encoding):
    results = face_recognition.compare_faces(
        [known_encoding], unknown_encoding)
    return results[0]
