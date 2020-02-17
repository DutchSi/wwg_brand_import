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
    features_list=features_list.split('.')
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

    bulletsList=bulletsList.split('.')
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
                        database='MASCOT',
                        user='python-user-1',
                        password='Cascadic77')
    

    if conn1.is_connected():
        sql_select_Query1 = "select * from MASCOT_extended_productdata_UK_en"
        cursor1 = conn1.cursor()
        cursor1.execute(sql_select_Query1)
        ext_prod_data = cursor1.fetchall()
        print("Total number of rows in MASCOT_ext_prod_data is: ", cursor1.rowcount)

        # sql_select_Query2 = "select * from MASCOT_MATERIAL_AVAILABILITY"
        # cursor2 = conn1.cursor()
        # cursor2.execute(sql_select_Query2)
        # mas_stock = cursor2.fetchall()
        # print("Total number of rows in MASCOT_MATERIAL_AVAILABILITY is: ", cursor2.rowcount)

        sql_select_Query9 = "select * from Pricelist_Januar2020_UK"
        cursor9 = conn1.cursor()
        cursor9.execute(sql_select_Query9)
        prices_2020 = cursor9.fetchall()
        print("Total number of rows in MASCOT_prices_2020 is: ", cursor9.rowcount)

        sql_select_Query10 = "select * from MASCOT_child_prod_codes"
        cursor10 = conn1.cursor()
        cursor10.execute(sql_select_Query10)
        child_prod_codes_data = cursor10.fetchall()
        print("Total number of rows in MASCOT_child_prod_codes is: ", cursor10.rowcount)

    else:
        print("ERROR - CANNOT ACCESS DB")


except Error as e:
    print ("UNABLE TO MAKE CONNECTION", e)
# finally:
#     #closing database connection.
#     if(conn1.is_connected()):
#         cursor1.close()
#         # cursor2.close()

productdb = mysql.connector.connect(host='cascadic-1.ckwr3sco1gnd.eu-west-2.rds.amazonaws.com',
                        database='products_dev',
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

    sql_select_Query8 = "select * from brand where brand = 'Mascot'"
    cursor8 = productdb.cursor()
    cursor8.execute(sql_select_Query8)
    brand_info = cursor8.fetchall()
    print("Total number of rows in PRODUCTS.brand is: ", cursor8.rowcount)

    gs1List=[]
    for a in gs1_info:
        b=[a,""]
        gs1List.append(b)
    # for c in gs1List:
    #     print("Hello")

    for i in range(len(cursor1.description)):
        if cursor1.description[i][0] == 'Colour Number':
            colour_number_heading=i
        if cursor1.description[i][0] == 'Product-Quality-Colour number':
            prod_qual_col_heading=i
        if cursor1.description[i][0] == 'EU Size':
            eu_size=i
        if cursor1.description[i][0] == 'EU Size Part 1':
            eu_size_part1=i
        if cursor1.description[i][0] == 'Volume':
            volume_heading=i
        if cursor1.description[i][0] == 'Weight':
            weight_heading=i
        if cursor1.description[i][0] == 'Product Type':
            product_type_heading=i
        if cursor1.description[i][0] == 'Product Categories':
            prod_cat_heading=i
        if cursor1.description[i][0] == 'Washing Symbol Name':
            washing_symbol_heading=i
        if cursor1.description[i][0] == 'Quality':
            quality_heading=i
        if cursor1.description[i][0] == 'USP text':
            usp_text_heading=i
        if cursor1.description[i][0] == 'Pictogram name':
            pictogram_name_heading=i
        if cursor1.description[i][0] == 'Pictogram text':
            pictogram_text_heading=i
        if cursor1.description[i][0] == 'Technical text':
            tech_text_heading=i
        if cursor1.description[i][0] == 'Quality remark':
            quality_remark_heading=i
        if cursor1.description[i][0] == 'Product-Quality number':
            prod_qual_no_heading=i
        if cursor1.description[i][0] == 'Range':
            range_heading=i
        if cursor1.description[i][0] == 'Quality weight':
            qual_weight_heading=i
        if cursor1.description[i][0] == 'Certification':
            certs_heading=i
        if cursor1.description[i][0] == 'EAN number':
            ean_heading=i
        # if cursor1.description[i][0] == '':
        #     _heading=i
        # if cursor1.description[i][0] == '':
        #     _heading=i
        
        for i in range(len(cursor5.description)):
                if cursor5.description[i][0] == 'mascot_no':
                    mascot_no_heading=i
                if cursor5.description[i][0] == 'name_uk':
                    name_uk_heading=i
        
        for i in range(len(cursor4.description)):
                if cursor4.description[i][0] == 'supplier_size1':
                    supplier_size1_heading=i
                if cursor4.description[i][0] == 'supplier_size2':
                    supplier_size2_heading=i    
                if cursor4.description[i][0] == 'plenty_be_name':
                    plenty_be_name_heading=i
                if cursor4.description[i][0] == 'amazon_name_uk':
                    amazon_name_uk_heading=i
                if cursor4.description[i][0] == 'amazon_name_us':
                    amazon_name_us_heading=i
                if cursor4.description[i][0] == 'comments':
                    comments_heading=i
                if cursor4.description[i][0] == 'brand':
                    brand_heading=i
                if cursor4.description[i][0] == 'ladies_fit':
                    ladies_fit_heading=i

mas_codes=[]
mas_parents=[]

for a in ext_prod_data:
    prod_code=a[6]
    if prod_code not in mas_codes:
        mas_parents.append(a)
        mas_codes.append(prod_code)

highest=0
for a in child_prod_codes_data:
    parent_sku_in=a[1]
    temp=str(parent_sku_in)[3:7]
    if int(temp) > int(highest):
        highest = int(temp)

highest+=1


for parent in mas_parents:
    new_sku_mkr=False
    child_iterator=1
    parent_sku_inheritor=""
    if parent[1] != "":
        sup_name=parent[product_type_heading]
        categories2=str(parent[prod_cat_heading])
        categories2=categories2.replace(';',',')
        washing=str(parent[washing_symbol_heading])
        washing=washing.replace(";",".")
        usp_text=str(parent[usp_text_heading])
        usp_text=usp_text.replace(";","")
        usp_text=usp_text.replace('\n',"")
        certs=str(parent[certs_heading])
        certs=certs.replace(';','.')

        pictogram=str(parent[pictogram_name_heading])
        pictogram_text=str(parent[pictogram_text_heading])
        tech_text=str(parent[tech_text_heading])
        tech_text=tech_text.replace('\n',"")
        quality_remark=str(parent[quality_remark_heading])
        prod_tag=""
        collection=""
        prop_tag=""
        prod_range=parent[range_heading]

        # POPULATE PARENT SKU
        product_id=parent[prod_qual_no_heading]
        found_mkr=False
        for a in child_prod_codes_data:
            if a[3] == product_id:
                sku = a[1]
                found_mkr=True
        
        if found_mkr==False:
            new_sku_mkr=True
            sku="MAS" + str(highest).zfill(4) + "P"
            
        parent_sku_inheritor=sku
        
        brand="Mascot"
        

        mycursor.execute("SELECT asin,ean FROM sku WHERE sku = %s", (sku,))
        # mycursor.execute("SELECT parent_sku, COUNT(*) FROM child WHERE sku = %s GROUP BY sku",(sku,))
        row_count = mycursor.rowcount
        sku_result = mycursor.fetchall()
        if row_count == 0:            
            # print ("First Load of sku info in sku table")
            sql_child = "INSERT INTO sku (sku,parent_sku,plenty_parent,asin,ean) VALUES (%s, %s, %s, %s, %s)"
            val_child = (sku,sku,"","","")
            mycursor.execute(sql_child, val_child)
            productdb.commit()
        else:
            print ("sku: " + sku + " already exists in sku table")
        
        # eguide_addition_en="(plus eBook)"
        gender_temp=parent[60]
        if gender_temp == "Children":
            gender = "Childrens"
            gender_tag=gender
            department="Boys"

        elif gender_temp == "Men" or gender_temp == "Men; Women" or gender_temp == "Men; Women; Children":
            gender = "Mens"
            gender_tag="Mens & Unisex"
            department="Men"

        elif gender_temp == "Women":
            gender = "Womens"
            gender_tag=gender
            department="Women"
        
        else:
            "ERROR - gender information could not be mapped"

        shopify_name=""
        amazon_name_en=""
        amazon_name_fr=""
        amazon_name_de=""
        amazon_name_it=""
        amazon_name_es=""
        amazon_name_us=""
        supplier_link_id=""
        
        # if float(vat) == 0:
        #     vat_tag = "VAT Free"
        # else:
        #     vat_tag = "Not VAT Free"
        vat_tag=""
        hivisind=""
        sleeve_type=""

        if "Hi-vis" in str(categories2):
            hivisind += "Hi-Vis"
            high_vis="Y"
        else:
            hivisind += "Not Hi-Vis"
            high_vis="N"

        if "Parka Jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Parka Jackets"
            category ="Parka Jackets"
            sleeve_type="Long Sleeve"

        if "Pilot jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Pilot Jackets"
            category ="Pilot Jackets"
            sleeve_type="Long Sleeve"
        
        if "Thermal Jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Thermal & Padded"
            category ="Thermal & Padded"
            sleeve_type="Long Sleeve"
        
        if "Winter Jackets" in str(categories2):
            sleeve_type="Long Sleeve"
            if prod_tag == "":
                prod_tag += "Clothing,Outerwear,Jackets,Winter Jackets"
                category ="Winter Jackets"
            else:
                prod_tag += ",Winter Jackets"

        if "Softshell Jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Softshell Jackets"
            category ="Softshell Jackets"
            sleeve_type="Long Sleeve"

        if "Outer Shell Jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Outer Shell Jackets"
            category ="Outer Shell Jackets"
            sleeve_type="Long Sleeve"
        
        if "Warehouse Coats" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Warehouse Coats"
            category ="Warehouse Coats"
            sleeve_type="Long Sleeve"

        if "Knitted Jackets" in str(categories2):
            prod_tag += "Clothing,Outerwear,Jackets,Knitted Jackets"
            category ="Knitted Jackets"
            sleeve_type="Long Sleeve"

        if "Gilets" in str(categories2):
            sleeve_type="Sleeveless"
            if "Tool Vests" in str(categories2):
                prod_tag += "Clothing,Outerwear,Bodywarmers Gilets & Vests,Tool Vests"
                category ="Tool Vests"
            else:
                prod_tag = "Clothing,Outerwear,Bodywarmers Gilets & Vests,Gilets"
                category = "Gilets"     

        if "¾" in str(categories2):
            prod_tag += "Clothing,Trousers Shorts Kilts Skirts,Shorts Pirate Shorts ¾ Trousers Kilts,Shorts Pirate Shorts ¾ trousers,Pirate Shorts & ¾ Trousers"
            category ="Pirate Shorts & ¾ Trousers"

        if "T-shirts" in str(categories2):
            prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,T-Shirts - Short & Long Sleeve"
            category ="T-Shirts - Short & Long Sleeve"
        
        if "Polo Shirts" in str(categories2):
            if "T-shirts" not in str(categories2):
                if "Sweatshirts" not in str(categories2):
                    prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,Polo Shirts"
                    category ="Polo Shirts"
                else:
                    prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,Polo Shirts,Clothing,Sweaters Fleeces & Hoodies,Sweatshirts"
                    category ="Polo Shirts"
        
        if "Kneepads" in str(categories2):
            prod_tag += "Accessories,Clothing Accessories,Knee Protection"
            category ="Knee Protection"
        
        if "Fleece J" in str(categories2):
            sleeve_type="Long Sleeve"
            prod_tag += "Clothing,Outerwear,Jackets,Fleece Jackets,Fleeces"
            category ="Fleece Jackets"   
        
        if "Jackets" in str(categories2) and prod_tag == "":
            prod_tag += "Clothing,Outerwear,Jackets"
            category ="Jackets"
            sleeve_type="Long Sleeve"
        
        
        
        if "Trousers" in str(categories2):
            if "Underwear" not in str(categories2):
                if prod_tag == "":
                    if "Jeans" in str(categories2):
                        prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Denim Trousers & Jeans,Jeans"
                        category ="Jeans"
                    elif "Over Trousers" in str(categories2):
                        prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Trousers,Rain & Over Trousers"
                        category ="Rain & Over Trousers"
                    elif "¾" in str(categories2) and prod_tag == "":
                        prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Shorts Pirate Shorts ¾ Trousers Kilts,Pirate Shorts & ¾ Trousers"
                        category ="Pirate Shorts & ¾ Trousers"
                    else:
                        prod_tag += "Clothing,Trousers Shorts Kilts & Skirts,Trousers"
                        category ="Trousers"
                else:
                    if "Jeans" in str(categories2):
                        prod_tag += ",Trousers Shorts Kilts & Skirts,Trousers,Jeans"
                    elif "Over Trousers" in str(categories2):
                        prod_tag += ",Trousers Shorts Kilts & Skirts,Trousers,Over Trousers"
                    elif "¾" in str(categories2):
                        prod_tag += ",Trousers Shorts Kilts & Skirts,Shorts Pirate Shorts ¾ Trousers Kilt,Pirate Shorts & ¾ Trousers"
                    else:
                        prod_tag += ",Trousers Shorts Kilts & Skirts,Trousers"
        
        if "Bib & braces" in str(categories2):
            prod_tag = "Clothing,Trousers Shorts Kilts & Skirts,Bib & Brace/Bib Trousers"
            category ="Bib & Brace/Bib Trousers"
        
        if "Sweatshirts" in str(categories2):
            sleeve_type="Long Sleeve"
            if "Polo Shirts" not in str(categories2):
                if prod_tag == "":
                    prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Sweatshirts"
                    category ="Sweatshirts"
                else:
                    prod_tag += ",Sweaters Fleeces & Hoodies,Sweatshirts"
        
        if "Hoodies" in str(categories2):
            prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Hoodies"
            category ="Hoodies"
            sleeve_type="Long Sleeve"
        
        if "Long-Sleeved Shirts" in str(categories2) or "Short-Sleeved Shirts" in str(categories2):
            prod_tag += "Clothing,T-Shirts Shirts & Polo Shirts,Shirts"
            category ="Shirts"
        
        if "Jumpers" in str(categories2) and ("Hoodies" not in str(categories2) or "Fleece" not in str(categories2) or "Jumper" not in str(categories2)) :
            sleeve_type="Long Sleeve"
            if "Sweatshirts" not in prod_tag:
                if prod_tag == "":
                    prod_tag += "Clothing,Sweaters Fleeces & Hoodies,Sweatshirts"
                    category ="Sweatshirts"
                else:
                    prod_tag += ",Sweaters Fleeces & Hoodies,Sweatshirts"
        
        if "Shorts" in str(categories2):
            if "Boxer" not in str(categories2):
                prod_tag += "Clothing,Trousers Shorts Kilts Skirts,Shorts Pirate Shorts ¾ Trousers Kilt,Shorts"
                category ="Shorts"
        
        if "Skirts" in str(categories2):
            prod_tag += "Clothing,Trousers Shorts Kilts Skirts,Skirts"
            category ="Skirts"
        
        if "Holster Pockets" in str(categories2):
            prod_tag += "Accessories,Clothing Accessories,Pockets"
            category ="Pockets"

        if "Overalls" in str(categories2):
            prod_tag += "Clothing,Outerwear,Coveralls/Overalls"
            category ="Coveralls/Overalls"
            sleeve_type="Long Sleeve"

        if "Under shirts" in str(categories2):
            prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Baselayers & Thermal Underwear,Tops"
            category ="Tops"
        
        if "Under Trousers" in str(categories2):
            prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Baselayers & Thermal Underwear,Bottoms"
            category ="Bottoms"

        if "Boxer Shorts" in str(categories2):
            prod_tag += "Clothing,Baselayers Thermal Underwear & Underwear,Underwear,Boxer Shorts"
            category ="Boxer Shorts"
        
        if "Balaclavas" in str(categories2):
            prod_tag += "Accessories,Headwear,Balaclavas"
            category ="Balaclavas"

        if "Knitted Hats" in str(categories2):
            prod_tag += "Accessories,Headwear,Beanies"
            category ="Beanies"

        if "Caps" in str(categories2):
            prod_tag += "Accessories,Headwear,Caps"
            category ="Caps"

        if "Hoods" in str(categories2):
            prod_tag += "Accessories,Headwear,Hoods"
            category ="Hoods"
        
        if "Belts" in str(categories2):
            if "Braces" in str(categories2):
                prod_tag += "Accessories,Belts & Braces,Braces"
                category ="Braces"
            else:
                prod_tag += "Accessories,Belts & Braces,Belts"
                category ="Belts"
        
        if "Socks" in str(categories2):
            prod_tag += "Accessories,Socks"
            category ="Socks"

        if "Neck Wamers" in str(categories2):
            prod_tag += "Accessories,Headwear,Scarves & Neckwarmers"
            category ="Scarves & Neckwarmers"
        
        if "Safety Boots" in str(categories2) or "Safety ankle boots" in str(categories2):
            prod_tag += "Footwear,Boots,Safety Boots"
            category ="Safety Boots"
        elif "Safety Shoes" in str(categories2) or "Safety footwear" in str(categories2):
            if "Safety Sandals" in str(categories2) or "clog" in str(sup_name).lower():
                prod_tag += "Footwear,Shoes,Safety Sandals & Clogs"
                category ="Safety Sandals & Clogs"
            else:
                prod_tag += "Footwear,Shoes,Safety Shoes"
                category ="Safety Shoes"
        elif "Safety Sandals" in str(categories2):
            if prod_tag == "":
                prod_tag += "Footwear,Shoes,Safety Sandals & Clogs"
                category ="Safety Sandals & Clogs"
        elif "Work shoes" in str(categories2):
            prod_tag += "Footwear,Trainers,Sports Shoes"
            category ="Sports Shoes"
        elif "Footwear" in str(categories2):
            if "work boots" in str(sup_name).lower():
                prod_tag += "Footwear,Trainers,Sports Shoes"
                category ="Sports Shoes"

        if "In Soles" in str(categories2):
            prod_tag += "Accessories,Other Footwear Accessories,Insoles"
            category ="Insoles"
        
        if "Accessories" in str(categories2) and prod_tag == "":
            prod_tag += "Accessories,All Other Accessories"
            category ="Accessories"
        
        # if "" in str(categories2):
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""
        
        # if "" in str(categories2):
        #     prod_tag += ""

        sleeve=""
        if sleeve_type=="":
            if "Long Sleeve" in str(categories2):
                if prop_tag == "":
                    prop_tag += "Long Sleeve"
                else:
                    prop_tag += ",Long Sleeve"
                sleeve_type="Long Sleeve"

            if "Short Sleeve" in str(categories2):
                if prop_tag == "":
                    prop_tag += "Short Sleeve"
                else:
                    prop_tag += ",Short Sleeve"
                sleeve_type="Short Sleeve"

        if "Waterproof Clothing" in str(categories2):
            if prop_tag == "":
                prop_tag += "Waterproof"

            else:
                prop_tag += ",Waterproof"
            waterproof="Y"
        else:
            waterproof="N"
        
        if "Winter clothing" in str(categories2):
            if prop_tag == "":
                prop_tag += "Winter Clothing,Winter"
            else:
                prop_tag += ",Winter Clothing,Winter"
            winter="Y"
        else:
            winter="N"

        if "Electrostatic Properties" in str(categories2):
            if prop_tag == "":
                prop_tag += "Anti-Static"
            else:
                prop_tag += ",Anti-Static"
            anti_static="Y"
        else:
            anti_static="N"

        if "Flame Retardent Clothing" in str(categories2):
            if prop_tag == "":
                prop_tag += "Flame Retardent"
            else:
                prop_tag += ",Flame Retardent"
            flame_retardent="Y"
        else:
            flame_retardent="N"

        if "Multi-protective" in str(categories2):
            if prop_tag == "":
                prop_tag += "Multi-Protective"
            else:
                prop_tag += ",Multi-Protective"
            multi_protective="Y"
        else:
            multi_protective="N"

        if "Electric arc tested" in str(categories2):
            if prop_tag == "":
                prop_tag += "Electric Arc Tested"
            else:
                prop_tag += ",Electric Arc Tested"
            electric_arc_tested="Y"
        else:
            electric_arc_tested="N"
        
        if "Against chemicals" in str(categories2):
            if prop_tag == "":
                prop_tag += "Chemical Resistant"
            else:
                prop_tag += ",Chemical Resistant"
            chemical_resistant="Y"
        else:
            chemical_resistant="N"
        
        if "UV Protective" in str(categories2):
            if prop_tag == "":
                prop_tag += "UV Protective"
            else:
                prop_tag += ",UV Protective"
            uv_protective="Y"
        else:
            uv_protective="N"
        
        if "Holster pocket" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Holster Pocket"
            else:
                prop_tag += ",Holster Pocket"
            holster_pocket="Y"
        else:
            holster_pocket="N"

        if "Kneepad pocket" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Knee Protection"
            else:
                prop_tag += ",Knee Protection"
            knee_protection="Y"
        else:
            knee_protection="N"
        
        if "Waterproof" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Waterproof"
            else:
                prop_tag += ",Waterproof"
            waterproof="Y"
        else:
            waterproof="N"
        
        if "Water-repellent" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Water resistant"
            else:
                prop_tag += ",Water resistant"
            water_resistant="Y"
        else:
            water_resistant="N"
        
        if "Windproof" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Windproof"
            else:
                prop_tag += ",Windproof"
            windproof="Y"
        else:
            windproof="N"
        
        if "Breathable" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Breathable"
            else:
                prop_tag += ",Breathable"
            breathable="Y"
        else:
            breathable="N"
        
        if "CORDURA" in str(tech_text):
            if prop_tag == "":
                prop_tag += "Cordura"
            else:
                prop_tag += ",Cordura"
            cordura="Y"
        else:
            cordura="N"
        
        if "BOA" in str(tech_text):
            if prop_tag == "":
                prop_tag += "Boa"
            else:
                prop_tag += ",Boa"
            boa="Y"
        else:
            boa="N"

        if "Dyneema" in str(tech_text):
            if prop_tag == "":
                prop_tag += "Dyneema"
            else:
                prop_tag += ",Dyneema"
            dyneema="Y"
        else:
            dyneema="N"
        
        # if "" in str(pictogram):
        #     if prop_tag == "":
        #         prop_tag += "Gore Tex"
        #     else:
        #         prop_tag += ",Gore Tex"
        
        if "Ripstop" in str(quality_remark):
            if prop_tag == "":
                prop_tag += "Ripstop"
            else:
                prop_tag += ",Ripstop"
            ripstop="Y"
        else:
            ripstop="N"

        if "goretex" in str(quality_remark):
            if prop_tag == "":
                prop_tag += "Goretex"
            else:
                prop_tag += ",Goretex"
            goretex="Y"
        else:
            goretex="N"

        if "Moisture wicking" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Moisture-wicking"
            else:
                prop_tag += ",Moisture-wicking"
            moisture_wicking="Y"
        else:
            moisture_wicking="N"
        
        if "Quick dry" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Quick Dry"
            else:
                prop_tag += ",Quick Dry"
            quick_dry="Y"
        else:
            quick_dry="N"
        
        if "Stain resistant" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Stain Resistant"
            else:
                prop_tag += ",Stain Resistant"
            stain_resistant="Y"
        else:
            stain_resistant="N"
        
        if "anti-bacterial" in str(usp_text).lower():
            if prop_tag == "":
                prop_tag += "Anti-Bacterial"
            else:
                prop_tag += ",Anti-Bacterial"
            anti_bacterial="Y"
        else:
            anti_bacterial="N"
        
        if "stretch" in str(usp_text).lower():
            if prop_tag == "":
                prop_tag += "Stretch"
            else:
                prop_tag += ",Stretch"
            stretch="Y"
        else:
            stretch="N"
        
        if "Toe Cap" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Toe Cap"
            else:
                prop_tag += ",Toe Cap"
            toe_cap="Y"
        else:
            toe_cap="N"
        
        if "Composite" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Composite"
            else:
                prop_tag += ",Composite"
            composite="Y"
        else:
            composite="N"
        
        if "Metal free" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Metal Free"
            else:
                prop_tag += ",Metal Free"
            metal_free="Y"
        else:
            metal_free="N"
        
        if "Oil" in str(pictogram_text) or "Petrol" in str(pictogram_text) or "Chemical" in str(pictogram_text):
            if prop_tag == "":
                prop_tag += "Oil Petrol or Chemical Resistant"
            else:
                prop_tag += ",Oil Petrol or Chemical Resistant"
            oil_resistant="Y"
        else:
            oil_resistant="N"
        
        if "Ultra Slip Resistant Sole" in str(certs):
            if prop_tag == "":
                prop_tag += "Slip Resistant/SLP"
            else:
                prop_tag += ",Slip Resistant/SLP"
            slip_resistant="Y"
        else:
            slip_resistant="N"
        
        if "°C" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Heat Resistant"
            else:
                prop_tag += ",Heat Resistant"
            heat_resistant="Y"
        else:
            heat_resistant="N"
        
        if "ESD" in str(pictogram):
            if prop_tag == "":
                prop_tag += "Anti-static"
            else:
                prop_tag += ",Anti-static"
            anti_static="Y"
        

        s1p="N"
        s1="N"
        s2="N"
        s3="N"
        s4="N"
        s5="N"
        if "Safety Class S1P" in str(certs):
            if prop_tag == "":
                prop_tag += "S1P"
            else:
                prop_tag += ",S1P"
            s1p="Y"
        elif "Safety Class S1" in str(certs):
            if prop_tag == "":
                prop_tag += "S1"
            else:
                prop_tag += ",S1"
            s1="Y"
        elif "Safety Class S2" in str(certs):
            if prop_tag == "":
                prop_tag += "S2"
            else:
                prop_tag += ",S2"
            s2="Y"
        elif "Safety Class S3" in str(certs):
            if prop_tag == "":
                prop_tag += "S3"
            else:
                prop_tag += ",S3"
            s3="Y"
        elif "Safety Class S4" in str(certs):
            if prop_tag == "":
                prop_tag += "S4"
            else:
                prop_tag += ",S4"
            s4="Y"
        elif "Safety Class S5" in str(certs):
            if prop_tag == "":
                prop_tag += "S5"
            else:
                prop_tag += ",S5"
            s5="Y"
        
        if "pearl fit" in str(pictogram).lower():
            ladies_fit += "Pearl"
            ladies_fit_tag = "Pearl Fit"
        elif "diamond fit" in str(pictogram).lower():
            ladies_fit += "Diamond"
            ladies_fit_tag = "Diamond Fit"
        else:
            ladies_fit = ""
            ladies_fit_tag = ""
        
        mycursor.execute("SELECT COUNT(*) FROM parent_features WHERE sku = %s GROUP BY sku",(sku,))

        row_count = mycursor.rowcount

        if row_count == 0:
            # print ("It Does Not Exist, Inserting")
            sql_parent_features = "INSERT INTO parent_features (sku,sleeve_type,holster_pocket,knee_protection,high_vis,stretch,waterproof,water_resistant,windproof,breathable,cordura,boa,dyneema,goretex,ripstop,moisture_wicking,quick_dry,stain_resistant,anti_bacterial,winter,anti_static,flame_retardent,multi_protective,electric_arc_tested,chemical_resistant,uv_protective,toe_cap,composite,metal_free,oil_resistant,heat_resistant,slip_resistant,S1,S1P,S2,S3,S4,S5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val_parent_features = (sku,sleeve_type,holster_pocket,knee_protection,high_vis,stretch,waterproof,water_resistant,windproof,breathable,cordura,boa,dyneema,goretex,ripstop,moisture_wicking,quick_dry,stain_resistant,anti_bacterial,winter,anti_static,flame_retardent,multi_protective,electric_arc_tested,chemical_resistant,uv_protective,toe_cap,composite,metal_free,oil_resistant,heat_resistant,slip_resistant,s1,s1p,s2,s3,s4,s5)
            mycursor.execute(sql_parent_features, val_parent_features)
            productdb.commit()
        else:
            try:
                # print ("It Does Exist, Inserting")
                sql_parent_features = "UPDATE parent_features SET sleeve_type=%s,holster_pocket=%s,knee_protection=%s,high_vis=%s,stretch=%s,waterproof=%s,water_resistant=%s,windproof=%s,breathable=%s,cordura=%s,boa=%s,dyneema=%s,goretex=%s,ripstop=%s,moisture_wicking=%s,quick_dry=%s,stain_resistant=%s,anti_bacterial=%s,winter=%s,anti_static=%s,flame_retardent=%s,multi_protective=%s,electric_arc_tested=%s,chemical_resistant=%s,uv_protective=%s,toe_cap=%s,composite=%s,metal_free=%s,oil_resistant=%s,heat_resistant=%s,slip_resistant=%s,s1=%s,s1p=%s,s2=%s,s3=%s,s4=%s,s5=%s WHERE sku=%s"
                val_parent_features = (sleeve_type,holster_pocket,knee_protection,high_vis,stretch,waterproof,water_resistant,windproof,breathable,cordura,boa,dyneema,goretex,ripstop,moisture_wicking,quick_dry,stain_resistant,anti_bacterial,winter,anti_static,flame_retardent,multi_protective,electric_arc_tested,chemical_resistant,uv_protective,toe_cap,composite,metal_free,oil_resistant,heat_resistant,slip_resistant,s1,s1p,s2,s3,s4,s5,sku)
                mycursor.execute(sql_parent_features, val_parent_features)
                productdb.commit()
            except Error as err:
                print("Update parent_features Error:{}".format(err))

        
        # if "" in str(certs):
        #     if prop_tag == "":
        #         prop_tag += ""
        #     else:
        #         prop_tag += ","
        

        # TEMPLATE in str(pictogram):
            # if prop_tag == "":
            #     prop_tag += ""
            # else:
            #     prop_tag += ","
            
        tags = gender_tag + "," + brand + "," + prod_tag + "," + vat_tag
        
        if prod_range != "":
            tags += "," + prod_range
        
        if hivisind != "":
            tags += "," + hivisind

        if ladies_fit_tag != "":
            tags += "," + ladies_fit_tag

        if prop_tag != "":
            tags += "," + prop_tag
        
        footwear_ind=False
        if "Footwear," in tags:
            footwear_ind=True
            
            if gender_temp == "Mens":
                target_gender="Male"
                footwear_gender="Men"
                age_range_description="Adult"
                footwear_age_group="Adult"
            elif gender_temp == "Men; Women; Children":
                target_gender="Unisex"
                footwear_gender="Men"
                age_range_description="Adult"
                footwear_age_group="Adult"
            elif gender_temp == "Men; Women":
                target_gender="Male"
                footwear_gender="Men"
                age_range_description="Adult"
                footwear_age_group="Adult"
            elif gender_temp == "Women":
                target_gender="Female"
                footwear_gender="Women"
                age_range_description="Adult"
                footwear_age_group="Adult"
            elif gender_temp == "Children":
                target_gender="Unisex"
                footwear_gender="Men"
                age_range_description="Kid"
                footwear_age_group="Big Kid"

        # if str(sku) == "JCB057P":
        #     print("STOP")

        mat_en=""
        certs_en=""
        removal_list=[]

        certs_en=certs

        washing_en=washing
        
        quality1=str(parent[quality_heading])
        quality2=str(parent[qual_weight_heading])
        mat_en=quality1+". "+quality2

        material = ""
        bullets1 = []
        bullets2 = []
        bulletsList = []
        text1=usp_text
        text2=tech_text
        bullets1 = text1.split('.')
        bullets2 = text2.split('.')
        bulletsBoth = []
        bullet1=""
        
        # Iterate through bullets in both lists to identify duplicates & store in list
        for bulletA in bullets1:
            bulletA=bulletA.lstrip()
            for bulletB in bullets2:
                bulletB=bulletB.lstrip()
                if bulletA == bulletB:
                    bulletsBoth.append(bulletA)
                if bulletB == "":
                    try:
                        bullets2.remove(bulletB)
                    except:
                        print("Error Processing")
            if bulletA=="":
                bullets1.remove(bulletA)

        # Add all bullets to list UNLESS they are a duplicate   
        for bulletA in bullets1:
            bulletA=bulletA.lstrip()
            bulletsList.append(bulletA)
        for bulletB in bullets2:
            mkr = True
            bulletB=bulletB.lstrip()
            for bulletC in bulletsBoth:
                if bulletB == bulletC:
                    mkr = False
            if mkr == True:
                bulletsList.append(bulletB)

        bulletsTextOut=""

        for a in bulletsList:
            bulletsTextOut += a + ". "

        # for bullet in bullets1:
        #     bullet1 = bullet.lstrip()
        #     if material.strip() in bullet1:
        #         bullets.remove(bullet)
        
        List1 = []
        for bt in bulletsList:
            List1.append([bt,False])
        
        # i=0
        # text2 = ""
        # if len(bullets1) > 0:
        #     text2 = "Features:"
        #     while i < len(bullets1):
        #         if i==0:
        #             text2 = bullets1[i]
        #         else:
        #             text2 += "\n" + bullets1[i].lstrip()
        #         i+=1

        # Length bullet x
        # If length bullet x < 100, add next bullet and check again. Remove from dictionary

        bullet1 = ""
        bullet2 = ""
        bullet3 = ""
        bullet4 = ""
        marker1 = False
        bulletList=[]
        bulletList2=[]
        a1=""
        a2=""
        a3=""
        a4=""
        a5=""
        no = 0

        marker1 = False
        while no < len(List1) and marker1 == False:
            if List1[no][1] == False:
                bullettemp = List1[no][0]
                if bullettemp != "":
                    bttemplen = len(bullettemp)
                    if len(a1) + bttemplen < 100:
                        if a1 == "":
                            a1 = List1[no][0]
                        else:
                            a1 += ". " + List1[no][0]
                        List1[no][1] = True
                        # marker1 = True
            no+=1
        # marker1 = False
       
        # WHAT IS THIS?    
        # if a1 == "" and len(material) < 100:
        #     a1 = material
        
        no = 0
        while no < len(List1) and marker1 == False:
            if List1[no][1] == False:
                bullettemp = List1[no][0]
                if bullettemp != "":
                    bttemplen = len(bullettemp)
                    if len(a2) + bttemplen < 100:
                        if a2 == "":
                            a2 = List1[no][0]
                        else:
                            a2 += ". " + List1[no][0]
                        List1[no][1] = True
                        # marker1 = True
            no+=1
        # marker1 = False

        no = 0
        while no < len(List1) and marker1 == False:
            if List1[no][1] == False:
                bullettemp = List1[no][0]
                if bullettemp != "":
                    bttemplen = len(bullettemp)
                    if len(a3) + bttemplen < 100:
                        if a3 == "":
                            a3 = List1[no][0]
                        else:
                            a3 += ". " + List1[no][0]
                        List1[no][1] = True
                        # marker1 = True
            no+=1
        # marker1 = False

        no = 0
        while no < len(List1) and marker1 == False:
            if List1[no][1] == False:
                bullettemp = List1[no][0]
                if bullettemp != "":
                    bttemplen = len(bullettemp)
                    if len(a4) + bttemplen < 100:
                        if a4 == "":
                            a4 = List1[no][0]
                        else:
                            a4 += ". " + List1[no][0]
                        List1[no][1] = True
                        # marker1 = True
            no+=1
        # marker1 = False

        no = 0
        while no < len(List1) and marker1 == False:
            if List1[no][1] == False:
                bullettemp = List1[no][0]
                if bullettemp != "":
                    bttemplen = len(bullettemp)
                    if len(a5) + bttemplen < 100:
                        if a5 == "":
                            a5 = List1[no][0]
                        else:
                            a5 += ". " + List1[no][0]
                        List1[no][1] = True
                        # marker1 = True
            no+=1
        
        bl=[a1,a2,a3,a4,a5]
        bulletList=(bl)

        # for bt in bulletList:
        #     # i=0
        #     # Populate 1st bullet
        #     # while i < len(List1) and marker1 == False:
        #     #     if (List1[i][1] == False):
        #     #         bullettemp = List1[i][0]
        #     #         bttemplen = len(bullettemp)
        #     #         if bttemplen < 100:
        #     #             bt = bullettemp
        #     #             List1[i][1] = True
        #     #             marker1 = True
        #     #     i+=1
        #     j=0
        #     while j < len(List1):
        #         length = len(bt)
        #         bullettemp = ""
        #         if (List1[j][1] == False):
        #             bullettemp = List1[j][0]
        #             lengthtemp = len(bullettemp)
        #             if bullettemp != "":
        #                 if (length + lengthtemp) < 98:
        #                     bt = bt + ". " + bullettemp
        #                     List1[j][1] = True
        #                     bullettemp=""
        #         j+=1
        #     marker1 = False
        #     bulletList2.append(bt)

        # rest=""
        # k=0
        # while k < len(List1) and marker1 == False:
        #         if (List1[k][1] == False):
        #             rest = List1[k][0]
        #             List1[k][1] = True
        #             marker1 = True
        #         k+=1
        #         l=0
        #         while l < len(List1):
        #             if (List1[l][1] == False):
        #                 rest += ", " + List1[l][0]
        #                 List1[l][1] = True
        #             l+=1


        mkr=1
        bul1=a1
        bul2=a2
        bul3=a3
        bul4=a4
        bul5=a5

        video = "https://www.youtube.com/watch?v=" + parent[73]

       
        payload = {
            'desc': "",
            'bullets': bulletsTextOut,
            'certs': certs_en,
            'material': mat_en,
            'washing': washing_en,
            'video' : video
        }


        # bundle_bullet="Tough, hardwearing JCB Workwear with eGuide (English language). Exclusive Workwear Gurus bundle."

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
        bullet1_en=bul1
        bullet2_en=bul2
        bullet3_en=bul3
        bullet4_en=bul4
        bullet5_en=bul5
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
        bullet1_us=bul1
        bullet2_us=bul2
        bullet3_us=bul3
        bullet4_us=bul4
        bullet5_us=bul5
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

        # prod_code_list=prod_code.split(',')
        code=parent[6]

        intrastat=parent[2]
        country_origin=parent[3]
        vat_rate=""
        
                


        # INTRASTAT/COUNTRY_ORIGIN/VAT POPULATED ABOVE
        # intrastat=""
        # country_origin=""
        # vat_rate=""

        images_to_load=""
        shipping_template="DEFAULT_WEIGHT"
        flag1="18"
        flag2="1"
        part_no=""
        model_no=""
        season_year="Winter/Spring 2020"
        no_items=""
        department=""
        inner_material=""
        outer_material=""
        style_code=""
        sleeve_type=""
        collar_style=""
        item_length=""
        waist_style=""
        closure=""
        sole_material=""
        heel_type=""
        heel_height=""
        heel_height_unit_of_measure="CM"
        target_gender=""
        age_range_description=""
        footwear_age_group=""
        footwear_gender=""
        footwear_size_class=""
        footwear_width=""
        special_features1=""
        special_features2=""
        special_features3=""
        special_features4=""
        special_features5=""
        hi_vis=""
        rrp_inc_vat=""

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
        for c in ext_prod_data:
            if c[6] == product_id:
                child_list.append(c)

        
        
        child_list.sort()
        
        highest_childsku_no=0
        for cl in child_prod_codes_data:
            if sku==cl[1] and 'P' not in cl[0]:
                temp=""
                temp_sku = cl[0]
                temp=temp_sku
                temp=str(temp)[7:10]
                if int(temp) > int(highest_childsku_no):
                    highest_childsku_no = int(temp)

        brand_discount=int(brand_info[0][5])/100
        
        child_sku_iterator=0
        for d in child_list:
   
            stock_size=""
            stock_cat=""
            buy_price=0
            
            stock_size1 = d[eu_size]
            stock_size2 = d[eu_size_part1]
            stock_colour_code = d[colour_number_heading]
            stock_code_col=d[prod_qual_col_heading]
            stock_colour_code=str(stock_colour_code).lstrip("0")
            buy_price=d[26] * (1-brand_discount)

            
            for c in colour_info:
                if stock_colour_code == c[mascot_no_heading]:
                    colour_name = c[name_uk_heading]
            
            size_id=""
            size_en=""
            size_us=""
            
            
            size_found_mkr=False
            for s in size_info:
                if s[brand_heading] == "MAS":
                    if footwear_ind==True:
                        lstriptemp=s[supplier_size1_heading].lstrip("0")
                        if str(stock_size1) == str(lstriptemp):
                            size_id=s[plenty_be_name_heading]
                            size_en=s[amazon_name_uk_heading]
                            size_us=s[amazon_name_us_heading]
                            size_found_mkr=True
                            break
                    # elif s[supplier_size2_heading] != "" and s[supplier_size2_heading][0] == "C":
                    if "Trousers" in category or "Shorts" in category or "Overalls" in category or "Skirts" in category or "Jeans" in category or "Jackets" in category or "Warehouse" in category:
                        if gender == "Mens":
                            if stock_size1 == s[supplier_size1_heading] and s[comments_heading] == "Mens":
                                size_id=s[plenty_be_name_heading]
                                size_en=s[amazon_name_uk_heading]
                                size_us=s[amazon_name_us_heading]
                                size_found_mkr=True
                                break
                        elif gender == "Womens":
                            if stock_size1 == s[supplier_size1_heading] and "Womens" in s[comments_heading]  and s[ladies_fit_heading] == ladies_fit:
                                size_id=s[plenty_be_name_heading]
                                size_en=s[amazon_name_uk_heading]
                                size_us=s[amazon_name_us_heading]
                                size_found_mkr=True
                                break
                    
                    if size_found_mkr==False and (stock_size2 == s[supplier_size2_heading] or stock_size1 == s[supplier_size1_heading]):
                        size_id=s[plenty_be_name_heading]
                        size_en=s[amazon_name_uk_heading]
                        size_us=s[amazon_name_us_heading]
                        size_found_mkr=True
                        break

            ean=""
            asin=""

            if size_id=="":
                print("No Size")

            
            
            # XXX - INSERT NAME HERE
            # XXX Add ladies fit info
            name_en=""+" - "+str(gender)+", "+str(size_en)+", "+str(colour_name)
            name_en.replace("  -"," -")
            name_fr=""
            name_de=""
            name_it=""
            name_es=""
            # XXX - INSERT NAME HERE
            # XXX Add ladies fit info
            name_us="" +str(gender)+", "+str(size_us)+", "+str(colour_name)
            name_us.replace("  -"," -")
            sup_sku=d[ean_heading]
            sup_barcode=d[ean_heading]
            main_barcode=""
            product_code_col=stock_code_col
            attributes="Size:"+str(size_id)+";Colour:"+str(colour_name)
            colour_id=colour_name

            # POPULATE CHILD SKU, EAN & ASIN
            # CHECK EXISTING WWG SKUS & EXTRACT INFO IF AVAILABLE (ALREADY CREATED)
            child_found_mkr=False
            for a in child_prod_codes_data:        
                if str(a[4])==str(sup_barcode) and "P" not in str(a[0]):
                    sku=a[0]
                    parent_sku= a[1]
                    ean = a[6]
                    asin = a[5]
                    child_found_mkr=True
                    break
                
            if sku=="MAS0061115":
                print("CHECK")

            # IF NOT CREATED PREVIOUSLY, CHECK IF CREATED PREVIOUSLY HERE
            if child_found_mkr==False:
                mycursor.execute("SELECT sku, COUNT(*) FROM sku WHERE supplier_sku = %s GROUP BY sku",(sup_barcode,))
                row_count = mycursor.rowcount
                sku_query_result = mycursor.fetchall()
                if row_count == 1:
                    sku=sku_query_result[0]
                    ean=query_result[4]
                    asin=query_result[3]
                    parent_sku=query_result[2]
                elif row_count==0:
                    for gs1 in gs1List:
                        if gs1[0][4] == "" and gs1[1] != "Y":
                            old_sku=gs1[0][0]
                            ean=gs1[0][2]
                            asin=gs1[0][3]
                            used_text="MASCOT Product Load"
                            gs1[1]="Y"
                            parent_sku=parent_sku_inheritor
                            sku=parent_sku[0:7]+str(highest_childsku_no+1).zfill(3)
                            highest_childsku_no+=1
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

            
            
            weight_temp=d[weight_heading].replace(',','.')
            if weight_temp=="":
                weight_g=""
            else:
                weight_g=float(weight_temp)*1000
            volume_temp=d[volume_heading].replace(',','.')
            volume=volume_temp
            length_mm=""
            width_mm=""
            height_mm=""
            
            image_main=""
            image_style=""
            image_detail=""
            images_to_load=""
            imagesList=[]

            # XXX - INSERT IMAGES WORK HERE
            images_to_load=""

            # SIZEGUIDE LOOKUP
            sizeguide_id=""
            if gender == "Childrens":
                sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Childrens.jpg"
            elif "Footwear," in tags:
                sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Shoes.jpg"
            elif "Outerwear" in tags or "Sweaters, Fleeces and hoodies" in tags or "T-shirts, Shirts & Polo Shirts" in tags:
                if gender == "Mens":
                    sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Men_Tops.jpg"
                elif gender == "Womens":
                    sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Women_Tops.jpg"
            elif "Trousers, Shorts, Kilts & Skirts" in tags:
                if gender == "Mens":
                    sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Men_Trousers.jpg"
                elif gender == "Womens":
                    sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_Women_Tops.jpg"
            elif "Baselayers, Thermal Underwear & Underwear" in tags or "Headwear" in tags:
                sizeguide_id = "https://cascadic.s3.eu-west-2.amazonaws.com/size_guides/Mascot_SizeGuide_default.jpg"

            bundle_image=''
            keywords_en=""
            keywords_fr=""
            keywords_de=""
            keywords_it=""
            keywords_es=""
            keywords_us=""

            # LOOKUP RRP PRICE
            for a in prices_2020:
                if sup_barcode == a[4]:
                    rrp_inc_vat=a[5]
                    break
            


            mycursor.execute("SELECT COUNT(*) FROM child WHERE sku = %s GROUP BY sku",(sku,))

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
                sql_child = "INSERT INTO child (sku,parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,main_barcode,asin,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,rrp_inc_vat,buy_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val_child = (sku,parent_sku,name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,ean,asin,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,rrp_inc_vat,buy_price)
                mycursor.execute(sql_child, val_child)
                productdb.commit()
            else:
                try:
                    # print ("It Does Exist, Inserting")
                    sql_child = "UPDATE child SET name_en=%s,name_fr=%s,name_de=%s,name_it=%s,name_es=%s,name_us=%s,sup_sku=%s,sup_barcode=%s,main_barcode=%s,asin=%s,product_code_col=%s,attributes=%s,colour_id=%s,size_id=%s,weight_g=%s,volume=%s,length_mm=%s,width_mm=%s,height_mm=%s,image_main=%s,image_style=%s,image_detail=%s,images_to_load=%s,sizeguide_id=%s,keywords_en=%s,keywords_fr=%s,keywords_de=%s,keywords_it=%s,keywords_es=%s,keywords_us=%s,rrp_inc_vat=%s,buy_price=%s WHERE sku=%s"
                    val_child = (name_en,name_fr,name_de,name_it,name_es,name_us,sup_sku,sup_barcode,ean,asin,product_code_col,attributes,colour_id,size_id,weight_g,volume,length_mm,width_mm,height_mm,image_main,image_style,image_detail,images_to_load,sizeguide_id,keywords_en,keywords_fr,keywords_de,keywords_it,keywords_es,keywords_us,rrp_inc_vat,buy_price,sku)
                    mycursor.execute(sql_parent, val_parent)
                    productdb.commit()
                except:
                    print("Unable to UPDATE CHILD for sku: " + sku)

            child_sku_iterator += 1
            print(sku)
        print(parent_sku)
        

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
    if new_sku_mkr==True:
        highest+=1
    
if(conn1.is_connected()):
        cursor1.close()

