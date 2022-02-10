# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
from IPython.display import display
import random
import json
import os
beard = ["beard"]
beard_weight = [1]
crown = ["crown"]
crow_weight = [1]
clothes = ["clothes"]
clothes_weight = [1]
ears = ["ears"]
ears_weights = [1]
eyeandBrow = ["eyeandBrow"]
eyeandBrow_weights = [1]
face = ["face1", "face2"]
face_weights = [1, 2]
hair = ["hair"]
hair_weights = [1]
neck = ["neck"]
neck_weights = [1]
nose = ["nose"]
nose_weights = [1]
face_files = {
    "face1":"sorat",
    "face2":"x"
}
ears_files = {
    "ears": "gosh"
}
eyeandBrow_file = {
    "eyeandBrow":"cheshmoabro"
}
hair_files = {
    "hair":"mo"
}
clothes_file = {
    "clothes":"lebas"
}
beard_file = {
    "beard":"rish"
}
neck_file = {
    "neck":"gardan"
}
nose_file = {
    "nose":"bini"
}
crown_file = {
    "crown":"taj"
}

TOTAL_IMAGES = 1

all_image = []

def create_image():
    new_image = {}

    new_image["Beard"] = random.choices(beard , beard_weight)[0]
    new_image["Clothes"] = random.choices(clothes , clothes_weight) [0]
    new_image ["Crown"] = random.choices(crown , crow_weight)[0]
    new_image["Face"] = random.choices(face, face_weights)[0]
    new_image["Ears"] = random.choices(ears, ears_weights)[0]
    new_image["EyeandBrow"] = random.choices(eyeandBrow, eyeandBrow_weights)[0]
    new_image["Hair"] = random.choices(hair, hair_weights)[0]
    new_image["Neck"] = random.choices(neck, neck_weights)[0]
    new_image["Nose"] =random.choices(nose , nose_weights)[0]

    if new_image in all_image :
        return  create_image()
    else:
        return new_image


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)
def trait_counting():
    face_count = {}
    for item in face:
        face_count[item] = 0

    ears_count = {}
    for item in ears:
        ears_count[item] = 0

    eyesandBrow_count = {}
    for item in eyeandBrow:
        eyesandBrow_count[item] = 0

    hair_count = {}
    for item in hair:
        hair_count[item] = 0

    neck_count = {}
    for item in neck:
        neck_count[item] = 0

    nose_count = {}
    for item in nose :
        nose_count[item] = 0

    crown_count = {}
    for item in crown :
        crown_count[item] = 0


    clothes_count = {}
    for item in clothes :
        clothes_count[item] = 0

    beard_count = {}
    for item in beard:
        beard_count[item] = 0

    for image in all_image :
        beard_count[image["Beard"]] += 1
        crown_count[image["Crown"]] += 1
        clothes_count[image["Clothes"]] += 1
        face_count[image["Face"]] +=1
        ears_count[image["Ears"]] +=1
        eyesandBrow_count[image["EyeandBrow"]] += 1
        hair_count[image["Hair"]] +=1
        neck_count[image["Neck"]] +=1
        nose_count[image["Nose"]] +=1


    # print(face_count)
    # print(ears_count)
    # print(eyesandBrow_count)
    # print(hair_count)
    # print(neck_count)
    # print(nose_count)
    # print(crown_count)
    # print(clothes_count)
    # print(beard_count)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello")

    create_image()
    for i in range(TOTAL_IMAGES):
        new_trait_image = create_image()

        all_image.append(new_trait_image)

    all_images_unique(all_image)
print("Are all images unique?", all_images_unique(all_image))

i = 0
for item in all_image:
    item["tokenId"] = i
    i = i + 1

print(all_image)
trait_counting()
for item in all_image:
    print(beard_file[item["Beard"]])
    img_beard = Image.open(f'assets /beard/{beard_file[item["Beard"]]}.png').convert('RGBA')
    print(img_beard)
    img_clothes = Image.open(f'assets /clothes/{clothes_file[item["Clothes"]]}.png').convert('RGBA')
    print(img_clothes)
    img_crown = Image.open(f'assets /crown/{crown_file[item["Crown"]]}.png').convert('RGBA')
    print(img_crown)
    img_ear = Image.open(f'assets /ear/{ears_files[item["Ears"]]}.png').convert('RGBA')
    print(img_ear)
    img_eyeAndBrow = Image.open(f'assets /eyeAndBrow/{eyeandBrow_file[item["EyeandBrow"]]}.png').convert('RGBA')
    print(img_eyeAndBrow)
    img_face = Image.open(f'assets /face/{face_files[item["Face"]]}.png').convert('RGBA')
    print(img_face)
    img_hair = Image.open(f'assets /hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    print(img_hair)
    img_neck = Image.open(f'assets /neck /{neck_file[item["Neck"]]}.png').convert('RGBA')
    print(img_neck)
    img_nose = Image.open(f'assets /noses/{nose_file[item["Nose"]]}.png').convert('RGBA')
    print(img_nose)


    com1 = Image.alpha_composite(img_face, img_eyeAndBrow)
    com2 = Image.alpha_composite(com1 , img_ear)
    com3 = Image.alpha_composite(com2 ,img_beard)
    com4 = Image.alpha_composite(com3 , img_beard)
    com5 = Image.alpha_composite(com4 , img_hair)
    com6 = Image.alpha_composite(com5 , img_nose)
    com7 = Image.alpha_composite(com6 , img_crown)
    # com5 = Image.alpha_composite(com4 , img_face)
    # com6 = Image.alpha_composite(com5 , img_hair)
    # com7 = Image.alpha_composite(com6 , img_neck)
    # com8 = Image.alpha_composite(com7 , img_nose)


    rgb_im = com7.convert('RGB')
    print(rgb_im)
    rgb_im.show()
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("assets/" + file_name)



