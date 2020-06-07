from puma_constants import *

def choose_category():
    GENDER = int(input('Принадлежность: \n1.Men \n2.Women\n3.Kids boys\n4.Kids girls\n'))
    CATEGORY = int(input('Категория: \n1.Shoes\n2.Clothing\n3.Аксессуары\n'))
    
    if GENDER == 1:
        GENDER = MEN
        if CATEGORY == 1:
            CATEGORY = SHOES           
            SHOES_CATEGORY = int(input('Тип:\n1.Lifestyle\n'
                                '2.Classics\n3.Training+Gym\n'
                                '4.Running\n5.Bassketball perfomance\n'
                                '6.Basketball\n7.Slides+sandals\n8.Motosport\n')
                                )
            if SHOES_CATEGORY == 1:
                SHOES_CATEGORY = LIFESTYLE
            elif SHOES_CATEGORY == 2:
                SHOES_CATEGORY = CLASSICS
            elif SHOES_CATEGORY == 3:
                SHOES_CATEGORY = TRAINING_GYM
            elif SHOES_CATEGORY == 4:
                SHOES_CATEGORY = RUNNING
            elif SHOES_CATEGORY == 5:
                SHOES_CATEGORY = BASSKETBALL_PERFOMANCE
            elif SHOES_CATEGORY == 6:
                SHOES_CATEGORY = BASSKETBALL
            elif SHOES_CATEGORY == 7:
                SHOES_CATEGORY = SLIDES_SANDALS
            elif SHOES_CATEGORY == 8:
                SHOES_CATEGORY = MOTOSPORT
            cgid = GENDER + CATEGORY + SHOES_CATEGORY
        if CATEGORY == 2:
            CATEGORY = CLOTHING            
            CLOTHING_CATEGORY = int(input('Тип:\n1.Shorts\n2.Sweatshirts+Hoodies\n'
                                '3.T-shirts + Tops\n4.Tracksuits\n5.Jackets\n'
                                '6.Pants\n'))
            if CLOTHING_CATEGORY == 1:
                CLOTHING_CATEGORY = SHORTS
            elif CLOTHING_CATEGORY == 2:
                CLOTHING_CATEGORY = SWEATSHIRTS_HOODIES
            elif CLOTHING_CATEGORY == 3:
                CLOTHING_CATEGORY = T_SHIRTS_TOPS
            elif CLOTHING_CATEGORY == 4:
                CLOTHING_CATEGORY = TRACKSUITS
            elif CLOTHING_CATEGORY == 5:
                CLOTHING_CATEGORY = JACKETS
            elif CLOTHING_CATEGORY == 6:
                CLOTHING_CATEGORY = PANTS
            cgid = GENDER + CATEGORY + CLOTHING_CATEGORY
        if CATEGORY == 3:
            CATEGORY = ACCESSORIES
            cgid = GENDER + CATEGORY

    if GENDER == 2:
        GENDER = WOMEN
        if CATEGORY == 1:
            CATEGORY = SHOES
            SHOES_CATEGORY = int(input('Тип:\n1.Lifestyle\n'
                                '2.Classics\n3.Training+Gym\n'
                                '4.Running\n5.Bassketball perfomance\n'
                                '6.Basketball\n7.Slides+sandals\n')
                            )
            if SHOES_CATEGORY == 1:
                SHOES_CATEGORY = LIFESTYLE
            elif SHOES_CATEGORY == 2:
                SHOES_CATEGORY = CLASSICS
            elif SHOES_CATEGORY == 3:
                SHOES_CATEGORY = TRAINING_GYM
            elif SHOES_CATEGORY == 4:
                SHOES_CATEGORY = RUNNING
            elif SHOES_CATEGORY == 5:
                SHOES_CATEGORY = BASSKETBALL_PERFOMANCE
            elif SHOES_CATEGORY == 6:
                SHOES_CATEGORY = BASSKETBALL
            elif SHOES_CATEGORY == 7:
                SHOES_CATEGORY = SLIDES_SANDALS
            cgid = GENDER + CATEGORY + SHOES_CATEGORY
        if CATEGORY == 2:
            CATEGORY = CLOTHING
            CLOTHING_CATEGORY = int(input('Тип:\n1.Shorts\n2.Sweatshirts+Hoodies\n'
                                '3.T-shirts + Tops\n4.Tracksuits\n5.Jackets\n'
                                '6.Pants\n7.Leggings\n8.Sports bras\n'))
            if CLOTHING_CATEGORY == 1:
                CLOTHING_CATEGORY = SHORTS
            elif CLOTHING_CATEGORY == 2:
                CLOTHING_CATEGORY = SWEATSHIRTS_HOODIES
            elif CLOTHING_CATEGORY == 3:
                CLOTHING_CATEGORY = T_SHIRTS_TOPS
            elif CLOTHING_CATEGORY == 4:
                CLOTHING_CATEGORY = TRACKSUITS
            elif CLOTHING_CATEGORY == 5:
                CLOTHING_CATEGORY = JACKETS
            elif CLOTHING_CATEGORY == 6:
                CLOTHING_CATEGORY = PANTS
            elif CLOTHING_CATEGORY == 7:
                CLOTHING_CATEGORY = LEGGINGS
            elif CLOTHING_CATEGORY == 8:
                CLOTHING_CATEGORY = BRAS
            cgid = GENDER + CATEGORY + CLOTHING_CATEGORY
        if CATEGORY == 3:
            CATEGORY = ACCESSORIES
            cgid = GENDER + CATEGORY
            
    if GENDER == 3:
        GENDER = KIDS_BOYS
        if CATEGORY == 1:
            CATEGORY = SHOES
        if CATEGORY == 2:
            CATEGORY = CLOTHING
        if CATEGORY == 3:
            CATEGORY = ACCESSORIES
        cgid = GENDER + CATEGORY
    
    if GENDER == 4:
        GENDER = KIDS_GIRLS
        if CATEGORY == 1:
            CATEGORY = SHOES
        if CATEGORY == 2:
            CATEGORY = CLOTHING
        if CATEGORY == 3:
            CATEGORY = ACCESSORIES
        cgid = GENDER + CATEGORY
            
    params = {
        'cgid': cgid,
        'start': 0,
        'sz': 2000,
        'isAjax': 1
    }

    print(cgid)
    return params