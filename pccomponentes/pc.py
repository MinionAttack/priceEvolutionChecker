import brands
import families

# LAPTOPS

__L_BRANDS = {'ACER': brands.ACER_ID, 'APPLE': brands.APPLE_ID, 'ASUS': brands.ASUS_ID, 'DELL': brands.DELL_ID,
              'FUJITSU': brands.FUJITSU_ID, 'GIGABYTE': brands.GIGABYTE_ID, 'HP': brands.HP_ID,
              'HUAWEI': brands.HUAWEI_ID, 'LENOVO': brands.LENOVO_ID, 'LG': brands.LG_ID, 'MEDION': brands.MEDION_ID,
              'MICROSOFT': brands.MICROSOFT_ID, 'MSI': brands.MSI_ID, 'SAMSUNG': brands.SAMSUNG_ID,
              'SCHNEIDER': brands.SCHNEIDER_ID, 'TOSHIBA': brands.TOSHIBA_ID, 'XIAOMI': brands.XIAOMI_ID}

Ls = {'FAMILY': families.L_FAMILY_ID, 'BRANDS': __L_BRANDS}

# PC DEKSTOP

__PCD_BRANDS = {'ACER': brands.ACER_ID, 'ASUS': brands.ASUS_ID, 'CORSAIR': brands.CORSAIR_ID, 'DELL': brands.DELL_ID,
                'HP': brands.HP_ID, 'MEDION': brands.MEDION_ID, 'MSI': brands.MSI_ID, 'OTHERS': brands.OTHERS_ID}

PCDs = {'FAMILY': families.PCD_FAMILY_ID, 'BRANDS': __PCD_BRANDS}

# MINI PC

__MPC_BRANDS = {'APPLE': brands.APPLE_ID, 'ASUS': brands.ASUS_ID, 'DELL': brands.DELL_ID,
                'GIGABYTE': brands.GIGABYTE_ID, 'INTEL': brands.INTEL_ID, 'LENOVO': brands.LENOVO_ID,
                'MEDION': brands.MEDION_ID, 'MINIX': brands.MINIX_ID, 'MSI': brands.MSI_ID, 'PRIMUX': brands.PRIMUX_ID,
                'QINTEX': brands.QINTEX_ID, 'RIKOMAGIC': brands.RIKOMAGIC_ID, 'OTHERS': brands.OTHERS_ID,
                'ZOTAC': brands.ZOTAC_ID}

MPCs = {'FAMILY': families.MPC_FAMILY_ID, 'BRANDS': __MPC_BRANDS}

# ALL IN ONE PC

__AIO_BRANDS = {'ACER': brands.ACER_ID, 'APPLE': brands.APPLE_ID, 'ASUS': brands.ASUS_ID, 'HP': brands.HP_ID,
                'LENOVO': brands.LENOVO_ID, 'LG': brands.LG_ID, 'MSI': brands.MSI_ID, 'SCHNEIDER': brands.SCHNEIDER_ID}

AIOs = {'FAMILY': families.AIO_FAMILY_ID, 'BRANDS': __AIO_BRANDS}

# SERVERS

__S_BRANDS = {'DELL': brands.DELL_ID, 'FUJITSU': brands.FUJITSU_ID, 'HP': brands.HP_ID}

Ss = {'FAMILY': families.S_FAMILY_ID, 'BRANDS': __S_BRANDS}
