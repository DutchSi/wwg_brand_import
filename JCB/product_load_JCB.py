def return_shopify_desc(payload):
    features_header = "<h3><strong>Features</strong></h3><ul>"
    washing_header = "<h3><strong>Washing Instructions</strong></h3>"
    certifications_header = "<h3><strong>Certifications</strong></h3>"
    material_header = "<h3><strong>Material Composition</strong></h3>"
    charset_start = "<meta charset=""utf-8"">"
    charset_end = "<meta charset=""utf-8"">"
    style = "<style type=""text/css""><!--td {border: 1px solid #ccc;}br {mso-data-placement:same-cell;}--></style>"
    para_start = "<ul>"
    para_end = "</ul>"
    bullet_start = "<li>"
    bullet_end = "</li>"
    line_start = "<p><span>"
    line_end = "</span></p>"
    para = "<p></p>"
    list_start = "<ul>"
    list_end = "</ul>"
    # embed_video_start = "<iframe width=""560"" height=""315"" src=""https://www.youtube.com/embed/"
    embed_video_start = "<iframe width=""560"" height=""315"" src=""https://www.youtube.com/embed/"
    # embed_video_end = " frameborder=""0"" allow=""accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"" allowfullscreen=""></iframe>"
    embed_video_end = " ""frameborder=""0"" allow=""accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"" allowfullscreen></iframe>"

    # GENERAL INFO
    # product_code = payload['']

    # AMAZON DESC
    desc = payload['desc']

    # FEATURES
    features_list = []
    feature_bullets=""
    # features = payload['bullets']
    features_list = payload['bullets']
    for c in features_list:
        if c != "":
            feature_bullets += bullet_start + c + bullet_end

    # WASHING INSTRUCTIONS
    washing = payload['washing']

    # MATERIAL INFO
    material_comp = payload['material']
    
    # CERTIFICATION
    certification = payload['certs']

    # YOUTUBE VIDEO
    youtube = payload['video']
    if youtube != "":
        video=embed_video_start + youtube + embed_video_end
    
    
    
    # PICTOGRAM REMOVED
    # description = video1 + features_header + charset_start + style + feature_bullets + list_end + para + pictogram + para + certifications_header + cert_bullets + list_end + para + material_header + line_start + material + line_end + washing_header + line_start + washing + line_end + charset_end
    # description = video + para + desc + para + features_header + charset_start + style + feature_bullets + list_end 

    description = ""

    # if video != "":
    #     description = video + para
    
    if desc != "":
        description = desc + para

    if feature_bullets != "":
        description = description + features_header + charset_start + style + feature_bullets + list_end
    
    if certification != "":
        description = description + para + certifications_header + line_start + certification + line_end 

    if material_comp != "":
        description = description + para + material_header + line_start + material_comp + line_end
    
    if washing !="":
        description = description + para + washing_header + line_start + washing + line_end
    
    description = description + charset_end

    # if extra_vids != "":
    #     description += extra_vids

    return description


def return_amazon_desc(payload):
    bulletsList=payload['bullets']
    cert_in=payload['certs']
    mat_in=payload['material']
    mat_text=""
    cert_text=""
    main_text=""

    if len(bulletsList) > 1:
        main_text = "<b>Features: </b> <br />"
        for a in bulletsList:
            if a != "":
                main_text += "- " + a + "<br />"

    # if features_text != "":
    #     main_text += "<br />" + features_text + "<br />"

    # if usp_text != "":
    #     main_text += description + "<br />"

    
    if cert_in != "":
        cert_text = "<b>Certifications: </b> <br />"
        cert_text += "- " + cert_in + "<br />"
        main_text += "<br />" + cert_text
    
    if mat_in != "":
        mat_text = "<b>Material: </b> <br />"
        mat_text += "- " + mat_in + "<br />"
        main_text += "<br />" + mat_text
    
    # if len(techList) > 1:
    #     tech_text = "<b>Technologies: </b> <br />"
    #     for a in techList:
    #         tech_text += "- " + a + "<br />"
    #     main_text += "<br />" + tech_text
    return main_text

import mysql.connector
from mysql.connector import Error
try:
    conn1 = mysql.connector.connect(host='cascadic-1.ckwr3sco1gnd.eu-west-2.rds.amazonaws.com',
                        database='JCB',
                        user='python-user-1',
                        password='Cascadic77')
    

    if conn1.is_connected():
        sql_select_Query1 = "select * from JCB_PRODUCTS"
        cursor1 = conn1.cursor()
        cursor1.execute(sql_select_Query1)
        jcb_products = cursor1.fetchall()
        print("Total number of rows in JCB_PRODUCTS is: ", cursor1.rowcount)

        sql_select_Query2 = "select * from Stockfile_200203"
        cursor2 = conn1.cursor()
        cursor2.execute(sql_select_Query2)
        jcb_stock = cursor2.fetchall()
        print("Total number of rows in JCB_STOCK is: ", cursor2.rowcount)

        sql_select_Query3 = "select * from Supplier_Product_Info"
        cursor3 = conn1.cursor()
        cursor3.execute(sql_select_Query3)
        jcb_sup_info = cursor3.fetchall()
        print("Total number of rows in JCB_SUPPLIER_PROD_INFO is: ", cursor3.rowcount)

        sql_select_Query6 = "select * from JCB_Listings_v1"
        cursor6 = conn1.cursor()
        cursor6.execute(sql_select_Query6)
        jcb_listings_v1 = cursor6.fetchall()
        print("Total number of rows in JCB_Listings_v1 is: ", cursor6.rowcount)
    else:
        print("ERROR - CANNOT ACCESS DB")


except Error as e:
    print ("UNABLE TO MAKE CONNECTION", e)
finally:
    #closing database connection.
    if(conn1.is_connected()):
        cursor1.close()
        cursor2.close()
        cursor3.close()
        conn1.close()

print("TEST")

productdb = mysql.connector.connect(host='cascadic-1.ckwr3sco1gnd.eu-west-2.rds.amazonaws.com',
                        database='products',
                        user='python-user-1',
                        password='Cascadic77')

mycursor = productdb.cursor(buffered=True)

if productdb.is_connected():
        sql_select_Query4 = "select * from size"
        cursor4 = productdb.cursor()
        cursor4.execute(sql_select_Query4)
        size_info = cursor4.fetchall()
        print("Total number of rows in PRODUCTS.size is: ", cursor4.rowcount)

        sql_select_Query5 = "select * from colour"
        cursor5 = productdb.cursor()
        cursor5.execute(sql_select_Query5)
        colour_info = cursor5.fetchall()
        print("Total number of rows in PRODUCTS.colour is: ", cursor5.rowcount)

        sql_select_Query7 = "select * from gs1_list"
        cursor7 = productdb.cursor()
        cursor7.execute(sql_select_Query7)
        gs1_info = cursor7.fetchall()
        print("Total number of rows in PRODUCTS.gs1 is: ", cursor7.rowcount)

        gs1List=[]
        for a in gs1_info:
            b=[a,""]
            gs1List.append(b)
        # for c in gs1List:
        #     print("Hello")

parent_sku_iterator=1
for parent in jcb_products:
    if parent[1] != "":

        prod_cat=parent[7]
        sup_name=parent[0]
        prod_info=parent[3]
        prod_code=str(parent[8])
        prod_tag=""
        collection=""
        prop_tag=""

        # POPULATE PARENT ENTRY
        sku="JCB" + str(parent_sku_iterator).zfill(3) + "P"
        brand="JCB"
        product_id=str(parent[8]).replace('/',',')
        prod_range=""

        mycursor.execute("SELECT * FROM sku WHERE sku = %s", (sku,))
        # mycursor.execute("SELECT parent_sku, COUNT(*) FROM child WHERE sku = %s GROUP BY sku",(sku,))
        row_count = mycursor.rowcount
        if row_count == 0:            
            # print ("First Load of sku info in sku table")
            sql_child = "INSERT INTO sku (sku,parent_sku,plenty_parent,asin,ean) VALUES (%s, %s, %s, %s, %s)"
            val_child = (sku,sku,"","","")
            mycursor.execute(sql_child, val_child)
            productdb.commit()
        else:
            print ("sku: " + sku + " already exists in sku table")
        
        if "essential" in str(sup_name).lower():
            prod_range="Essential"
        elif "trade" in str(sup_name).lower():
            prod_range="Trade"
        elif "limited edition" in str(sup_name).lower():
            prod_range="Limited Edition" 
        else:   
            prod_range=""
        
        eguide_addition_en="(plus eBook)"
        gender="Mens"

        shopify_name=parent[1]
        amazon_name_en=parent[1]+" - "+gender+" "+eguide_addition_en
        amazon_name_en.replace("  -"," -")
        amazon_name_fr=""
        amazon_name_de=""
        amazon_name_it=""
        amazon_name_es=""
        amazon_name_us=parent[2]+" - "+gender+" "+eguide_addition_en
        amazon_name_us.replace("  -"," -")
        supplier_link_id=""
        
        # cat=jcb_products[3]
        
        # if "high vis" in str(prod_cat).lower() or "high vis" in str(sup_name).lower():
        #     hivisind += "Hi-Vis"
        # else:
        #     hivisind += "Not Hi-Vis"

        # if "multinorm" in str(sup_name).lower() or "flame retardant" in str(sup_name).lower() or "flame retardent" in str(sup_name).lower() or "anti-flame" in str(sup_name).lower() or "welding" in str(sup_name).lower():
        #     safeind += "Safety"
        
        if ("coats" in str(prod_cat).lower() or "jackets" in str(prod_cat).lower()):
            if "parka" in str(sup_name).lower():
                prod_tag += "Clothing,Outerwear,Jackets,Parka Jackets"
                collection = "Jackets"
                category = "Parka Jackets"
            elif "pilot" in str(sup_name).lower():
                prod_tag += "Clothing,Outerwear,Jackets,Pilot Jackets"
                collection = "Jackets"
                category = "Pilot Jackets"
            elif "winter" in str(sup_name).lower():
                if prod_tag == "":
                    prod_tag += "Clothing,Outerwear,Jackets,Winter Jackets"
                    collection = "Jackets"
                    category = "Winter Jackets"
                else:
                    prod_tag += ",Winter Jackets"
            elif ("soft shell" in str(sup_name).lower() or "softshell" in str(sup_name).lower()):
                prod_tag += "Clothing,Outerwear,Jackets,Softshell Jackets"
                collection = "Jackets"
                category = "Softshell Jackets"
            elif "rain" in str(sup_name).lower():
                prod_tag += "Clothing,Outerwear,Jackets,Rain & Shell Jackets"
                collection = "Jackets"
                category = "Rain & Shell Jackets"
            elif "gilet" in str(sup_name):
                prod_tag += "Clothing,Outerwear,Bodywarmers Gilets & Vests,Gilets"
                collection = "Bodywarmers Gilets & Vests"
                category = "Gilets"
            elif "padded jacket" in str(sup_name):
                prod_tag += "Clothing,Outerwear,Jackets,Fleece Jackets,Thermal & Padded"
                collection = "Jackets"
                category = "Thermal & Padded"
            else:
                prod_tag += "Clothing,Outerwear,Jackets"
                collection = "Jackets"
                category = "Jackets"

            if "fleece" in str(sup_name).lower() or "pile" in str(sup_name).lower():
                if prod_tag == "":
                    prod_tag += "Clothing,Outerwear,Jackets,Fleece Jackets"
                    collection = "Jackets"
                    category = "Fleece Jackets"
                else:
                    prod_tag += ",Clothing,Outerwear,Jackets,Fleece Jackets"
        
        if "foul weather" in str(prod_cat).lower():
            prod_tag += "Clothing,Outerwear,Jackets,Rain & Shell Jackets,Rain and Over Trousers,Rain and Over Trousers"
            collection = "Jackets,Trousers"
            category = "Rain & Shell Jackets"
        
        # if "Thermal Jackets" in str(categories2):
        #     prod_tag += "Clothing,Outerwear,Jackets,Thermal & Padded Jackets"
        #     collection = "Jackets"
        
        
        # if "Warehouse Coats" in str(categories2):
        #     prod_tag += "Clothing,Outerwear,Jackets,Warehouse Coats"
        #     collection = "Jackets"

        

        # if "waistcoats" in str(prod_cat).lower():
        #     if "vest" in str(sup_name).lower():
        #         prod_tag += "Clothing,Outerwear,Bodywarmers Gilets & Vests,Tool Vests"
        #         collection = "Bodywarmers Gilets & Vests"
        #     else:
        #         prod_tag += "Clothing,Outerwear,Bodywarmers Gilets & Vests,Gilets"
        #         collection += "Bodywarmers Gilets & Vests"     

        if "shorts" in str(sup_name).lower():
            prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Shorts ¾ Trousers & Kilts,Shorts"
            collection = "Shorts ¾ Trousers & Kilts"
            category = "Shorts"

        if "polo" in str(sup_name).lower():
            prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,Polo Shirts"
            collection = "Polo Shirts"
            category = "Polo Shirts"
            if "long sleeve" in str(sup_name).lower():
                if prop_tag == "":
                    prop_tag += "Long Sleeve"
                else:
                    prop_tag += ",Long Sleeve"
            else:
                if prop_tag == "":
                    prop_tag += "Short Sleeve"
                else:
                    prop_tag += ",Short Sleeve"
        
        if "t-shirt" in str(sup_name).lower():
            prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,T-Shirts - Short & Long Sleeve,T-Shirts"
            collection = "T-Shirts - Short & Long Sleeve"
            category = "T-Shirts - Short & Long Sleeve"
            if "long sleeve" in str(sup_name).lower():
                if prop_tag == "":
                    prop_tag += "Long Sleeve"
                else:
                    prop_tag += ",Long Sleeve"
            else:
                if prop_tag == "":
                    prop_tag += "Short Sleeve"
                else:
                    prop_tag += ",Short Sleeve"
        
        
        # if "Jackets" in str(categories2) and prod_tag == "":
        #     prod_tag += "Clothing,Outerwear,Jackets"
        #     collection = "Jackets"
        
        
        
        if "trousers" in str(prod_cat).lower():
            if prod_tag == "":
                if "jeans" in str(sup_name).lower():
                    prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Trousers,Denim Trousers & Jeans"
                    collection = "Denim Trousers & Jeans"
                    category = "Denim Trousers & Jeans"
                elif "rain trousers" in str(prod_cat).lower():
                    prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Trousers,Rain and Over Trousers"
                    collection = "Rain and Over Trousers"
                    category = "Rain and Over Trousers"
                else:
                    prod_tag += "Trousers Shorts Kilts Skirts,Trousers"
                    collection = "Trousers"
                    category = "Trousers"
            else:
                if "jeans" in str(sup_name).lower():
                    prod_tag += ",Trousers Shorts Kilts & Skirts,Trousers,Denim Trousers & Jeans"
                    collection = "Denim Trousers & Jeans"
                    category = "Denim Trousers & Jeans"
                else:
                    prod_tag += "Trousers Shorts Kilts Skirts,Trousers"
                    collection = "Trousers"
                    category = "Trousers"
        
        if "sweatshirt" in str(prod_cat).lower():
            if prod_tag == "":
                prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Sweatshirts"
                collection = "Sweatshirts"
                category = "Sweatshirts"
            else:
                prod_tag += ",Sweaters Fleeces & Hoodies,Sweatshirts"
        
        if "jumper" in str(sup_name).lower():
            prod_tag += "Clothing,Outerwear,Sweaters Fleeces & Hoodies,Knitted Jumpers & Jackets,Knitted Jackets"
            collection = "Knitted Jumpers & Jackets"
            category = "Knitted Jackets"
        
        if "hoodie" in str(sup_name).lower():
            prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Hoodies"
            collection = "Hoodies"
            category = "Hoodies"

        # if "tops" in str(prod_cat).lower():
        #     prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,Shirts"
        #     collection = "Shirts"

        
        if "coveralls" in str(prod_cat).lower():
            prod_tag += "Clothing,Outerwear,Coveralls/Overalls,Overalls"
            collection = "Coveralls/Overalls"
            category = "Coveralls/Overalls"

        if "thermal wear" in str(prod_cat).lower():
            if "sleeve" in str(sup_name).lower():
                prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Baselayers & Thermal Underwear,Tops"
                collection = "Baselayers & Thermal Underwear"
                category = "Tops"
            elif "pants" in str(sup_name).lower():
                prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Baselayers & Thermal Underwear,Bottoms"
                collection = "Baselayers & Thermal Underwear"
                category = "Bottoms"
        
        # if "underwear" in str(prod_cat).lower() and ("pants" in str(sup_name).lower():
        #     prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Baselayers & Thermal Underwear,Bottoms"
        #     collection = "Baselayers & Thermal Underwear"

        # if "underwear" in str(prod_cat).lower() and ("boxer" in str(sup_name).lower() or "hipster" in str(sup_name).lower()):
        #     prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Underwear,Boxer Shorts"
        #     collection = "Underwear"
        
        # if "underwear" in str(prod_cat).lower() and "bra" in str(sup_name).lower():
        #     prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Underwear,Bras"
        #     collection = "Underwear"
        
        # if "underwear" in str(prod_cat).lower() and "underwear set" in str(sup_name).lower():
        #     prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Underwear"
        #     collection = "Underwear"
        
        if "fleece" in str(prod_cat).lower():
            if prod_tag == "":
                prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Fleeces"
                collection = "Fleeces"
                category = "Fleeces"
            if "jacket" in str(sup_name).lower():
                if prod_tag == "":
                    prod_tag += "Clothing,Outerwear,Jackets,Fleece Jackets"
                    collection = "Jackets"
                    category = "Fleece Jackets"
                else:
                    prod_tag += ",Clothing,Outerwear,Jackets,Fleece Jackets"
        
        # if "accessories" in str(prod_cat).lower() and "balaclava" in str(sup_name).lower():
        #     prod_tag += "Accessories,Clothing Accessories,Headwear,Balaclavas"
        #     collection = "Headwear"

        if "accessories" in str(prod_cat).lower():
            if "beanie" in str(sup_name).lower():
                prod_tag += "Accessories,Clothing Accessories,Headwear,Beanies"
                collection = "Headwear"
                category = "Beanies"
            elif "hat" in str(sup_name).lower():
                prod_tag += "Accessories,Clothing Accessories,Headwear,Hats"
                collection = "Headwear"
                category = "Hats"
            else:
                prod_tag += "Accessories,Clothing Accessories,Headwear"
                collection = "Headwear"
                category = "Headwear"

        # if "accessories" in str(prod_cat).lower() and "cap " in str(sup_name).lower():
        #     prod_tag += "Accessories,Clothing Accessories,Headwear,Caps"
        #     collection = "Headwear"
        
        
        if "kneepads" in str(sup_name).lower():
            prod_tag += "Accessories,Clothing Accessories,Knee Protection"
            collection = "Knee Protection"
            category = "Knee Protection"
        
        
        if "gloves" in str(sup_name).lower():
            prod_tag += "Accessories,Clothing Accessories,Gloves"
            collection = "Gloves"
            category = "Gloves"
        
        if "accessories" in str(prod_cat).lower():
            if "belt" in str(sup_name).lower():
                prod_tag += "Accessories,Clothing Accessories,Belts & Braces,Belts"
                collection = "Belts & Braces"
                category = "Belts"
        
        if "socks" in str(sup_name).lower():
            prod_tag += "Accessories,Clothing Accessories,Socks"
            collection = "Socks"
            category = "Socks"

        # if "accessories" in str(prod_cat).lower() and ("neck warmer" in str(sup_name).lower() or "collar" in str(sup_name).lower()):
        #     prod_tag += "Accessories,Clothing Accessories,Headwear,Scarves & Neckwarmers"
        #     collection = "Headwear"
        
        if "safety boots" in str(prod_cat).lower() or "dealer" in str(prod_cat).lower():
            if "boot" in str(sup_name).lower():
                prod_tag += "Footwear,Boots,Safety Boots"
                collection = "Safety Boots"
                category = "Safety Boots"
            elif "shoe" in str(sup_name).lower():
                prod_tag += "Footwear,Safety Shoes"
                collection = "Safety Shoes"
                category = "Safety Shoes"
        elif "safetytrainers" in str(prod_cat).lower():
            prod_tag += "Footwear,Trainers,Safety Trainers"
            collection = "Safety Trainers"
            category = "Safety Trainers"
        elif "wellingtons" in str(prod_cat).lower():
            prod_tag += "Footwear,Boots, Wellingtons & Waders"
            collection = "Wellingtons & Waders"
            category = "Wellingtons & Waders"
        elif "hikers" in str(prod_cat).lower():
            prod_tag += "Footwear,Boots,Hiking Boots"
            collection = "Hiking Boots"
            category = "Hiking Boots"

        # if "Work shoes" in str(categories2):
        #     prod_tag += "Footwear,Trainers,Sports Shoes"
        #     collection = "Sports Shoes"

        # if "accessories" in str(prod_cat).lower() and "insole" in str(sup_name).lower():
        #     prod_tag += "Accessories,Footwear Accessories,Other Footwear Accessories,Insoles"
        #     collection = "Insoles"
        
        # if ("accessories" in str(prod_cat).lower() and "lace" in str(sup_name).lower()):
        #     prod_tag += "Accessories,Footwear Accessories,Other Footwear Accessories,Laces"
        #     collection = "Laces"
        
        # if "accessories" in str(prod_cat).lower() and ("lace" not in str(sup_name).lower() and "insoles" not in str(sup_name).lower()) and "shoe" in str(sup_name).lower():
        #     prod_tag += "Accessories,Footwear Accessories,Other Footwear Accessories"
        #     collection = "Other Footwear Accessories"
        
        if "miscellaneous" in str(prod_cat).lower():
            prod_tag += "Accessories,Other Accessories,All Other Accessories"
            collection = "All Other Accessories"
            category = "All Other Accessories"
        
        # if "" in str(categories2):    
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""

        
        
        category=category

        if prop_tag=="":
            tags=prod_tag
        else:
            tags=prod_tag+","+prop_tag

        gender="Mens"

        prod_info_list=prod_info.split(',')

        # if str(sku) == "JCB057P":
        #     print("STOP")

        mat_en=""
        certs_en=""
        removal_list=[]

        for a in prod_info_list:
            a.replace('â€“','')
            if ('%' in a or 'gsm' in a) and 'batteries' not in a:
                if mat_en == "":
                    mat_en += a
                else:
                    mat_en += "," + a 
                # prod_info_list.remove(a)
                removal_list.append(a)
                
            elif 'EN ISO' in a or "S3" in a or 'SRA' in a or 'EN388' in a or 'Certified to EN' in a or 'Type 2 Level 0' in a:
                if certs_en == "":
                    certs_en += a
                else:
                    certs_en += "," + a 
                # prod_info_list.remove(a)
                removal_list.append(a)

        for rl in removal_list:
            for a in prod_info_list:
                if rl == a:
                    prod_info_list.remove(rl)


        mkr=1
        bul1=""
        bul2=""
        bul3=""
        bul4=""
        bul5=""
        for a in prod_info_list:
            if mkr == 1:
                if bul1=="":
                    bul1+=a
                else:
                    bul1+=". " + a
            elif mkr == 2:
                if bul2=="":
                    bul2+=a
                else:
                    bul2+=". " + a
            elif mkr == 3:
                if bul3=="":
                    bul3+=a
                else:
                    bul3+=". " + a
            elif mkr == 4:
                if bul4=="":
                    bul4+=a
                else:
                    bul4+=". " + a
            # CHANGING DUE TO ADDITION OF EGUIDE
            # elif mkr == 5:
            #     if bul5=="":
            #         bul5+=a
            #     else:
            #         bul5+=". " + a
            # if mkr==5:
            #     mkr=1
            # else:
            #     mkr+=1
            if mkr==4:
                mkr=1
            else:
                mkr+=1
            
            # EGUIDE BULLET
            bul_eguide_en=""
        
        payload = {
            'desc': "",
            'bullets': prod_info_list,
            'certs': certs_en,
            'material': mat_en,
            'washing': "",
            'video' : ""
        }


        bundle_bullet="Tough, hardwearing JCB Workwear with eGuide (English language). Exclusive Workwear Gurus bundle."

        description_shopify=return_shopify_desc(payload)

        description_amazon_en=return_amazon_desc(payload)

        description_amazon_fr=""
        description_amazon_de=""
        description_amazon_it=""
        description_amazon_es=""
        description_amazon_us=return_amazon_desc(payload)
        # bullet1_en=bul1
        # bullet2_en=bul2
        # bullet3_en=bul3
        # bullet4_en=bul4
        # bullet5_en=bul5
        bullet1_en=bundle_bullet
        bullet2_en=bul1
        bullet3_en=bul2
        bullet4_en=bul3
        bullet5_en=bul4
        bullet1_fr=""
        bullet2_fr=""
        bullet3_fr=""
        bullet4_fr=""
        bullet5_fr=""
        bullet1_de=""
        bullet2_de=""
        bullet3_de=""
        bullet4_de=""
        bullet5_de=""
        bullet1_it=""
        bullet2_it=""
        bullet3_it=""
        bullet4_it=""
        bullet5_it=""
        bullet1_es=""
        bullet2_es=""
        bullet3_es=""
        bullet4_es=""
        bullet5_es=""
        # CHANGING DUE TO EGUIDE ADDITION
        # bullet1_us=bul1
        # bullet2_us=bul2
        # bullet3_us=bul3
        # bullet4_us=bul4
        # bullet5_us=bul5
        bullet1_us=bundle_bullet
        bullet2_us=bul1
        bullet3_us=bul2
        bullet4_us=bul3
        bullet5_us=bul4
        material_en=mat_en
        material_fr=""
        material_de=""
        material_it=""
        material_es=""
        material_us=""
        certifications_en=certs_en
        certifications_fr=""
        certifications_de=""
        certifications_it=""
        certifications_es=""
        certifications_us=""
        washing_en=""
        washing_fr=""
        washing_de=""
        washing_it=""
        washing_es=""
        washing_us=""

        prod_code_list=prod_code.split(',')
        code=prod_code_list[0]

        intrastat=""
        country_origin=""
        vat_rate=""
        
        
        for b in jcb_sup_info:
            if code in b[1]:
                intrastat=b[8]
                country_origin=b[9]
                if int(b[7]) == 1:
                    vat_rate=20
                    tags += ",Not VAT Free"
                elif int(b[7]) == 3:
                    vat_rate=0
                    tags += ",VAT Free"
                break
                


        # INTRASTAT/COUNTRY_ORIGIN/VAT POPULATED ABOVE
        # intrastat=""
        # country_origin=""
        # vat_rate=""

        images_to_load=""
        video=""
        shipping_template="DEFAULT_WEIGHT"
        flag1="17"
        flag2="1"
        part_no=""
        model_no=prod_code.replace('/',',')
        season_year="Winter/Spring 2020"
        no_items=parent[9]
        department=parent[10]
        inner_material=parent[11]
        outer_material=parent[12]
        style_code=parent[13]
        sleeve_type=parent[14]
        collar_style=parent[15]
        item_length=parent[16]
        waist_style=parent[17]
        closure=parent[18]
        sole_material=parent[19]
        heel_type=parent[20]
        heel_height=parent[21]
        heel_height_unit_of_measure="CM"
        target_gender=parent[23]
        age_range_description=parent[24]
        footwear_age_group=parent[25]
        footwear_gender=parent[26]
        footwear_size_class=parent[27]
        footwear_width=parent[28]
        special_features1=parent[29]
        special_features2=parent[30]
        special_features3=parent[31]
        special_features4=parent[32]
        special_features5=parent[33]
        hi_vis=""
        rrp_inc_vat=parent[34]

        # temp1="sku,brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,supplier_link_id,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,material_en,material_fr,material_dr,material_it,material_es,material_us,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,certifications_us,washing_en,washing_fr,washing_de,washing_it,washing_es,washing_us,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis"
        # temp1_list=temp1.split(',')
        # print(len(temp1_list))

        # temp2="sku,brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,supplier_link_id,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,mat_en,material_fr,material_de,material_it,material_es,material_us,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,certifications_us,washing_en,washing_fr,washing_de,washing_it,washing_es,washing_us,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis"
        # temp2_list=temp2.split(',')
        # print(len(temp2_list))

        # temp3="%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
        # temp3_list=temp3.split(',')
        # print(len(temp3_list))

        # temp2="brand=%s,product_id=%s,prod_range=%s,shopify_name=%s,amazon_name_en=%s,amazon_name_fr=%s,amazon_name_de=%s,amazon_name_it=%s,amazon_name_es=%s,amazon_name_us=%s,supplier_link_id=%s,category=%s,tags=%s,gender=%s,description_shopify=%s,description_amazon_en=%s,description_amazon_fr=%s,description_amazon_de=%s,description_amazon_it=%s,description_amazon_es=%s,description_amazon_us=%s,bullet1_en=%s,bullet2_en=%s,bullet3_en=%s,bullet4_en=%s,bullet5_en=%s,bullet1_fr=%s,bullet2_fr=%s,bullet3_fr=%s,bullet4_fr=%s,bullet5_fr=%s,bullet1_de=%s,bullet2_de=%s,bullet3_de=%s,bullet4_de=%s,bullet5_de=%s,bullet1_it=%s,bullet2_it=%s,bullet3_it=%s,bullet4_it=%s,bullet5_it=%s,bullet1_es=%s,bullet2_es=%s,bullet3_es=%s,bullet4_es=%s,bullet5_es=%s,bullet1_us=%s,bullet2_us=%s,bullet3_us=%s,bullet4_us=%s,bullet5_us=%s,material_en=%s,material_fr=%s,material_de=%s,material_it=%s,material_es=%s,certifications_en=%s,certifications_fr=%s,certifications_de=%s,certifications_it=%s,certifications_es=%s,washing_en=%s,washing_fr=%s,washing_de=%s,washing_it=%s,washing_es=%s,intrastat=%s,country_origin=%s,vat_rate=%s,images_to_load=%s,video=%s,shipping_template=%s,flag1=%s,flag2=%s,part_no=%s,model_no=%s,season_year=%s,no_items=%s,department=%s,inner_material=%s,outer_material=%s,style_code=%s,sleeve_type=%s,collar_style=%s,item_length=%s,waist_style=%s,closure=%s,sole_material=%s,heel_type=%s,heel_height=%s,heel_height_unit_of_measure=%s,target_gender=%s,age_range_description=%s,footwear_age_group=%s,footwear_gender=%s,footwear_size_class=%s,footwear_width=%s,=%s,special_features2=%s,special_features3=%s,special_features4=%s,special_features5=%s,hi_vis=%s"
        # temp2_list=temp2.split(',')
        # print(len(temp2_list))

        # temp3="brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,supplier_link_id,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,mat_en,material_fr,material_de,material_it,material_es,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,washing_en,washing_fr,washing_de,washing_it,washing_es,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis,sku"
        # temp3_list=temp3.split(',')
        # print(len(temp3_list))

        mycursor.execute(
            "SELECT sku, COUNT(*) FROM parent WHERE sku = %s GROUP BY sku",
            (sku,)
        )
        # gets the number of rows affected by the command executed
        row_count = mycursor.rowcount
        # print ("number of affected rows: {}".format(row_count))
        if row_count == 0:
            # print ("It Does Not Exist, Inserting")
            sql_parent = "INSERT INTO parent (sku,brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,material_en,material_fr,material_de,material_it,material_es,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,washing_en,washing_fr,washing_de,washing_it,washing_es,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val_parent = (sku,brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,mat_en,material_fr,material_de,material_it,material_es,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,washing_en,washing_fr,washing_de,washing_it,washing_es,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis)
            mycursor.execute(sql_parent, val_parent)
            productdb.commit()
        else:
            # print ("It Does Exist, Inserting")
            sql_parent = "UPDATE parent SET brand=%s,product_id=%s,prod_range=%s,shopify_name=%s,amazon_name_en=%s,amazon_name_fr=%s,amazon_name_de=%s,amazon_name_it=%s,amazon_name_es=%s,amazon_name_us=%s,category=%s,tags=%s,gender=%s,description_shopify=%s,description_amazon_en=%s,description_amazon_fr=%s,description_amazon_de=%s,description_amazon_it=%s,description_amazon_es=%s,description_amazon_us=%s,bullet1_en=%s,bullet2_en=%s,bullet3_en=%s,bullet4_en=%s,bullet5_en=%s,bullet1_fr=%s,bullet2_fr=%s,bullet3_fr=%s,bullet4_fr=%s,bullet5_fr=%s,bullet1_de=%s,bullet2_de=%s,bullet3_de=%s,bullet4_de=%s,bullet5_de=%s,bullet1_it=%s,bullet2_it=%s,bullet3_it=%s,bullet4_it=%s,bullet5_it=%s,bullet1_es=%s,bullet2_es=%s,bullet3_es=%s,bullet4_es=%s,bullet5_es=%s,bullet1_us=%s,bullet2_us=%s,bullet3_us=%s,bullet4_us=%s,bullet5_us=%s,material_en=%s,material_fr=%s,material_de=%s,material_it=%s,material_es=%s,certifications_en=%s,certifications_fr=%s,certifications_de=%s,certifications_it=%s,certifications_es=%s,washing_en=%s,washing_fr=%s,washing_de=%s,washing_it=%s,washing_es=%s,intrastat=%s,country_origin=%s,vat_rate=%s,images_to_load=%s,video=%s,shipping_template=%s,flag1=%s,flag2=%s,part_no=%s,model_no=%s,season_year=%s,no_items=%s,department=%s,inner_material=%s,outer_material=%s,style_code=%s,sleeve_type=%s,collar_style=%s,item_length=%s,waist_style=%s,closure=%s,sole_material=%s,heel_type=%s,heel_height=%s,heel_height_unit_of_measure=%s,target_gender=%s,age_range_description=%s,footwear_age_group=%s,footwear_gender=%s,footwear_size_class=%s,footwear_width=%s,special_features1=%s,special_features2=%s,special_features3=%s,special_features4=%s,special_features5=%s,hi_vis=%s WHERE sku = %s"
            val_parent = (brand,product_id,prod_range,shopify_name,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,category,tags,gender,description_shopify,description_amazon_en,description_amazon_fr,description_amazon_de,description_amazon_it,description_amazon_es,description_amazon_us,bullet1_en,bullet2_en,bullet3_en,bullet4_en,bullet5_en,bullet1_fr,bullet2_fr,bullet3_fr,bullet4_fr,bullet5_fr,bullet1_de,bullet2_de,bullet3_de,bullet4_de,bullet5_de,bullet1_it,bullet2_it,bullet3_it,bullet4_it,bullet5_it,bullet1_es,bullet2_es,bullet3_es,bullet4_es,bullet5_es,bullet1_us,bullet2_us,bullet3_us,bullet4_us,bullet5_us,mat_en,material_fr,material_de,material_it,material_es,certifications_en,certifications_fr,certifications_de,certifications_it,certifications_es,washing_en,washing_fr,washing_de,washing_it,washing_es,intrastat,country_origin,vat_rate,images_to_load,video,shipping_template,flag1,flag2,part_no,model_no,season_year,no_items,department,inner_material,outer_material,style_code,sleeve_type,collar_style,item_length,waist_style,closure,sole_material,heel_type,heel_height,heel_height_unit_of_measure,target_gender,age_range_description,footwear_age_group,footwear_gender,footwear_size_class,footwear_width,special_features1,special_features2,special_features3,special_features4,special_features5,hi_vis,sku)
            mycursor.execute(sql_parent, val_parent)
            productdb.commit()
        
        mycursor.execute("SELECT parent_sku, COUNT(*) FROM child WHERE sku = %s GROUP BY sku",(sku,))

        # gets the number of rows affected by the command executed
        row_count = mycursor.rowcount
        # print ("number of affected rows: {}".format(row_count))

        # temp3="%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
        # temp3_list=temp3.split(',')
        # print(len(temp3_list))

        # temp2="brand=%s,product_id=%s,prod_range=%s,shopify_name=%s,amazon_name_en=%s,amazon_name_fr=%s,amazon_name_de=%s,amazon_name_it=%s,amazon_name_es=%s,amazon_name_us=%s,supplier_link_id=%s,category=%s,tags=%s,gender=%s,description_shopify=%s,description_amazon_en=%s,description_amazon_fr=%s,description_amazon_de=%s,description_amazon_it=%s,description_amazon_es=%s,description_amazon_us=%s,bullet1_en=%s,bullet2_en=%s,bullet3_en=%s,bullet4_en=%s,bullet5_en=%s,bullet1_fr=%s,bullet2_fr=%s,bullet3_fr=%s,bullet4_fr=%s,bullet5_fr=%s,bullet1_de=%s,bullet2_de=%s,bullet3_de=%s,bullet4_de=%s,bullet5_de=%s,bullet1_it=%s,bullet2_it=%s,bullet3_it=%s,bullet4_it=%s,bullet5_it=%s,bullet1_es=%s,bullet2_es=%s,bullet3_es=%s,bullet4_es=%s,bullet5_es=%s,bullet1_us=%s,bullet2_us=%s,bullet3_us=%s,bullet4_us=%s,bullet5_us=%s,material_en=%s,material_fr=%s,material_de=%s,material_it=%s,material_es=%s,certifications_en=%s,certifications_fr=%s,certifications_de=%s,certifications_it=%s,certifications_es=%s,washing_en=%s,washing_fr=%s,washing_de=%s,washing_it=%s,washing_es=%s,intrastat=%s,country_origin=%s,vat_rate=%s,images_to_load=%s,video=%s,shipping_template=%s,flag1=%s,flag2=%s,part_no=%s,model_no=%s,season_year=%s,no_items=%s,department=%s,inner_material=%s,outer_material=%s,style_code=%s,sleeve_type=%s,collar_style=%s,item_length=%s,waist_style=%s,closure=%s,sole_material=%s,heel_type=%s,heel_height=%s,heel_height_unit_of_measure=%s,target_gender=%s,age_range_description=%s,footwear_age_group=%s,footwear_gender=%s,footwear_size_class=%s,footwear_width=%s,=%s,special_features2=%s,special_features3=%s,special_features4=%s,special_features5=%s,hi_vis=%s"
        # temp2_list=temp2.split(',')
        # print(len(temp2_list))

        if row_count == 0:
            # print ("It Does Not Exist, Inserting")
            sql_child = "INSERT INTO child (sku,parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val_child = (sku,sku,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,)
            mycursor.execute(sql_child, val_child)
            productdb.commit()
        else:
            # print ("It Does Exist, Inserting")
            sql_child = "UPDATE child SET parent_sku=%s,name_en=%s,name_fr=%s,name_de=%s,name_it=%s,name_es=%s,name_us=%s WHERE sku=%s"
            val_child = (sku,amazon_name_en,amazon_name_fr,amazon_name_de,amazon_name_it,amazon_name_es,amazon_name_us,sku)
            mycursor.execute(sql_parent, val_parent)
            productdb.commit()


        

        # print(mycursor.rowcount, "record inserted.")

        child_list=[]
        # if 'F/TRACK' in prod_code_list:
        #     print("F/TRACK")
        for c in jcb_stock:
            if c[8] in prod_code_list:
                child_list.append(c)
        
        child_list.sort()
        
        

        
        
        child_sku_iterator=0
        for d in child_list:
   
            stock_size=""
            stock_cat=""
            buy_price=0
            for c in jcb_stock:
                if c[3] == child_list[child_sku_iterator][3]:
                    stock_size = c[5]
                    stock_name = c[6]
                    stock_colour = c[9]
                    stock_cat = c[1]
                    stock_code_col=c[0]
                    buy_price=c[10]
                    break
            
            if stock_size == "X3L":
                stock_size = "XXXL"
            elif stock_size == "N/A":
                stock_size = "One Size"
            # elif "Footwear" in stock_cat:
            #     stock_size = stock_size + " UK"
            if "trousers" in stock_cat.lower():
                if "short" in stock_name.lower():
                    stock_size = stock_size + " Short"
                elif "regular" in stock_name.lower():
                    stock_size = stock_size + " Reg"
            if "coverall" in stock_cat.lower():
                if "regular leg" in stock_name.lower():
                    stock_size = stock_size + " (Reg Leg)"
                elif "tall leg" in stock_name.lower():
                    stock_size = stock_size + " (Tall Leg)"
            
            size_id=""
            size_en=""
            size_us=""
            for s in size_info:
                if stock_size == s[5] and s[4] == "JCB":
                    size_id = s[0]
                    size_en = s[6]
                    size_us = s[11]
                    break
            
            # POPULATE CHILD ENTRY
            sku="JCB" + str(parent_sku_iterator).zfill(3) + str(child_sku_iterator+1).zfill(3)
            parent_sku="JCB" + str(parent_sku_iterator).zfill(3) + "P"

            ean=""
            asin=""

            mycursor.execute("SELECT sku, COUNT(*) FROM gs1_list WHERE sku = %s GROUP BY sku",(sku,))
            row_count = mycursor.rowcount
            if row_count == 1:
                # row = mycursor.fetchone()
                # ean=row[2]
                # asin=row[3]
                for gs1 in gs1List:
                    if gs1[0][0] == sku:
                        ean=gs1[0][2]
                        asin=gs1[0][3]
                        break
            elif row_count==0:
                for gs1 in gs1List:
                    if gs1[0][4] == "" and gs1[1] != "Y":
                        old_sku=gs1[0][0]
                        ean=gs1[0][2]
                        asin=gs1[0][3]
                        used_text="JCB Product Load"
                        gs1[1]="Y"
                        sql_child = "UPDATE gs1_list SET sku=%s,used=%s,old_sku=%s,updated=%s WHERE sku=%s"
                        val_child = (sku,used_text,old_sku,"Y",old_sku)
                        mycursor.execute(sql_child, val_child)
                        productdb.commit()
                        break
            else:
                print("WTF IS GOING ON, MORE THAN 2 ENTRIES!!!")



            mycursor.execute("SELECT sku, COUNT(*) FROM sku WHERE sku = %s GROUP BY sku",(sku,))
            row_count = mycursor.rowcount
            if row_count == 0:
                # print ("First Load of sku info in sku table")
                sql_child = "INSERT INTO sku (sku,parent_sku,plenty_parent,asin,ean) VALUES (%s, %s, %s, %s, %s)"
                val_child = (sku,parent_sku,parent_sku,asin,ean)
                mycursor.execute(sql_child, val_child)
                productdb.commit()
            

            name_en=parent[1]+" - "+gender+", "+size_en+", "+stock_colour+" "+eguide_addition_en
            name_en.replace("  -"," -")
            name_fr=""
            name_de=""
            name_it=""
            name_es=""
            name_us=parent[2]+" - "+gender+", "+size_us+", "+stock_colour+" "+eguide_addition_en
            name_us.replace("  -"," -")
            sup_sku=child_list[child_sku_iterator][4    ]
            sup_barcode=child_list[child_sku_iterator][3]
            main_barcode=""
            product_code_col=stock_code_col
            attributes="Size:"+size_id+";Colour:"+stock_colour
            colour_id=stock_colour
            
            weight_g=""
            volume=""
            length_mm=""
            width_mm=""
            height_mm=""
            
            for e in jcb_sup_info:
                if str(e[5]) == str(child_list[child_sku_iterator][3]):
                    print(str(e[5]))
                    weight_g=e[10]
                    if str(e[11]) != "" and str(e[11]) != "TBC":
                        length_mm=float(e[11])*10
                    if str(e[12]) != "" and str(e[12]) != "TBC":
                        width_mm=float(e[12])*10
                    if str(e[13]) != "" and str(e[13]) != "TBC":
                        height_mm=float(e[13])*10
                    break
            
            image_main=""
            image_style=""
            image_detail=""
            images_to_load=""
            imagesList=[]

            for old in jcb_listings_v1:
                if old[0] == product_code_col and old[37] != "":
                    images=str(old[37])
                    images=images.replace(',,,','')
                    images=images.replace(',,','')
                    imagesList=old[37].split(',')
                    for il in imagesList:
                        if "Size_Chart" not in il:
                            if il != "":
                                if images_to_load == "":
                                    images_to_load += il
                                else:
                                    images_to_load += "," + il
                    break
            
            if product_code_col == 'D-4X':
                images_to_load = 'https://cascadic.s3.eu-west-2.amazonaws.com/prodductimages/JCB/D-4X.jpg'
            elif product_code_col == '3CX/H':
                images_to_load = 'https://cascadic.s3.eu-west-2.amazonaws.com/prodductimages/JCB/3CX+HONEY+R.png,https://cascadic.s3.eu-west-2.amazonaws.com/prodductimages/JCB/3CX%3AH.jpg'
            

            
            sizeguide_id="https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/JCB_SizeGuide.jpg"
            bundle_image='https://cascadic.s3.eu-west-2.amazonaws.com/Miscellaneous/Kitted-Up+book+image+v0.2.jpg'
            keywords_en=""
            keywords_fr=""
            keywords_de=""
            keywords_it=""
            keywords_es=""
            keywords_us=""
            rrp_inc_vat=float(parent[34])

            if images_to_load == "":
                images_to_load += sizeguide_id + "," + bundle_image
            else:
                images_to_load += "," + sizeguide_id + "," + bundle_image

            mycursor.execute("SELECT parent_sku, COUNT(*) FROM child WHERE sku = %s GROUP BY sku",(sku,))

            # gets the number of rows affected by the command executed
            row_count = mycursor.rowcount
            # print ("number of affected rows: {}".format(row_count))

            # temp3="%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
            # temp3_list=temp3.split(',')
            # print(len(temp3_list))

            # temp2="brand=%s,product_id=%s,prod_range=%s,shopify_name=%s,amazon_name_en=%s,amazon_name_fr=%s,amazon_name_de=%s,amazon_name_it=%s,amazon_name_es=%s,amazon_name_us=%s,supplier_link_id=%s,category=%s,tags=%s,gender=%s,description_shopify=%s,description_amazon_en=%s,description_amazon_fr=%s,description_amazon_de=%s,description_amazon_it=%s,description_amazon_es=%s,description_amazon_us=%s,bullet1_en=%s,bullet2_en=%s,bullet3_en=%s,bullet4_en=%s,bullet5_en=%s,bullet1_fr=%s,bullet2_fr=%s,bullet3_fr=%s,bullet4_fr=%s,bullet5_fr=%s,bullet1_de=%s,bullet2_de=%s,bullet3_de=%s,bullet4_de=%s,bullet5_de=%s,bullet1_it=%s,bullet2_it=%s,bullet3_it=%s,bullet4_it=%s,bullet5_it=%s,bullet1_es=%s,bullet2_es=%s,bullet3_es=%s,bullet4_es=%s,bullet5_es=%s,bullet1_us=%s,bullet2_us=%s,bullet3_us=%s,bullet4_us=%s,bullet5_us=%s,material_en=%s,material_fr=%s,material_de=%s,material_it=%s,material_es=%s,certifications_en=%s,certifications_fr=%s,certifications_de=%s,certifications_it=%s,certifications_es=%s,washing_en=%s,washing_fr=%s,washing_de=%s,washing_it=%s,washing_es=%s,intrastat=%s,country_origin=%s,vat_rate=%s,images_to_load=%s,video=%s,shipping_template=%s,flag1=%s,flag2=%s,part_no=%s,model_no=%s,season_year=%s,no_items=%s,department=%s,inner_material=%s,outer_material=%s,style_code=%s,sleeve_type=%s,collar_style=%s,item_length=%s,waist_style=%s,closure=%s,sole_material=%s,heel_type=%s,heel_height=%s,heel_height_unit_of_measure=%s,target_gender=%s,age_range_description=%s,footwear_age_group=%s,footwear_gender=%s,footwear_size_class=%s,footwear_width=%s,=%s,special_features2=%s,special_features3=%s,special_features4=%s,special_features5=%s,hi_vis=%s"
            # temp2_list=temp2.split(',')
            # print(len(temp2_list))

            if row_count == 0:
                # print ("It Does Not Exist, Inserting")
                sql_child = "INSERT INTO child (sku,parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,main_barcode,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,rrp_inc_vat,buy_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val_child = (sku,parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,ean,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,rrp_inc_vat,buy_price)
                mycursor.execute(sql_child, val_child)
                productdb.commit()
            else:
                # print ("It Does Exist, Inserting")
                sql_child = "UPDATE child SET parent_sku=%s,name_en=%s,name_fr=%s,name_de=%s,name_it=%s,name_es=%s,name_us=%s,sup_sku=%s,sup_barcode=%s,main_barcode=%s,product_code_col=%s,attributes=%s,colour_id=%s,size_id=%s,weight_g=%s,volume=%s,length_mm=%s,width_mm=%s,height_mm=%s,image_main=%s,image_style=%s,image_detail=%s,images_to_load=%s,sizeguide_id=%s,keywords_en=%s,keywords_fr=%s,keywords_de=%s,keywords_it=%s,keywords_es=%s,keywords_us=%s,rrp_inc_vat=%s,buy_price=%s WHERE sku=%s"
                val_child = (parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,ean,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,sku,rrp_inc_vat,buy_price)
                mycursor.execute(sql_parent, val_parent)
                productdb.commit()

            child_sku_iterator += 1
        print(parent_sku)
        parent_sku_iterator +=1

    # OW UPDATING ABOVE ONE BY ONE
    # for gs1 in gs1_info:
    #     if gs1[7] == "Y":
    #         sku_replace=gs1[0]
    #         sql_child = "INSERT INTO gs1_list (sku,used,old_sku,updated) VALUES (%s, %s, %s, %s,)"
    #         val_child = (gs1[0],gs1[4],gs1[6],gs1[7])
    #         mycursor.execute(sql_child, val_child)
    #         productdb.commit()
    productdb.commit()


    # print(mycursor.rowcount, "record inserted.")


