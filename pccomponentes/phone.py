import brands
import families

# SMARTPHONES

__SP_BRANDS = {'ACER': brands.ACER_ID, 'ALCATEL': brands.ALCATEL_ID, 'ASUS': brands.ASUS_ID, 'BLU': brands.BLU_ID,
               'BQ': brands.BQ_ID, 'BRIGMTON': brands.BRIGMTON_ID, 'CAT': brands.CAT_ID,
               'CROSSCALL': brands.CROSSCALL_ID, 'CUBOT': brands.CUBOT_ID, 'ELEPHONE': brands.ELEPHONE_ID,
               'ENERGY_SISTEM': brands.ENERGY_SISTEM_ID, 'GIGASET': brands.GIGASET_ID, 'GOOGLE': brands.GOOGLE_ID,
               'HAIER': brands.HAIER_ID, 'HISENSE': brands.HISENSE_ID, 'HONOR': brands.HONOR_ID,
               'HUAWEI': brands.HUAWEI_ID, 'INEW': brands.INEW_ID, 'INNJOO': brands.INNJOO_ID,
               'LENOVO': brands.LENOVO_ID, 'LEOTEC': brands.LEOTEC_ID, 'LG': brands.LG_ID, 'MEIZU': brands.MEIZU_ID,
               'MICROSOFT': brands.MICROSOFT_ID, 'MOTOROLA': brands.MOTOROLA_ID, 'NOKIA': brands.NOKIA_ID,
               'NUBIA': brands.NUBIA_ID, 'OEM': brands.OEM_ID, 'ONEPLUS': brands.ONEPLUS_ID, 'RAZER': brands.RAZER_ID,
               'SAMSUNG': brands.SAMSUNG_ID, 'SISWOO': brands.SISWOO_ID, 'SONY': brands.SONY_ID,
               'SONY_ERICSSON': brands.SONY_ERICSSON_ID, 'TPLINK': brands.TPLINK_ID, 'ULEFONE': brands.ULEFONE_ID,
               'VIVO': brands.VIVO_ID, 'WEIMEI': brands.WEIMEI_ID, 'WIKO': brands.WIKO_ID, 'WOLDER': brands.WOLDER_ID,
               'XIAOMI': brands.XIAOMI_ID, 'ZTE': brands.ZTE_ID, 'ZUK': brands.ZUK_ID}

SPs = {'FAMILY': families.SP_FAMILY_ID, 'BRANDS': __SP_BRANDS}

# BASIC PHONES

__BP_BRANDS = {'ALCATEL': brands.ALCATEL_ID, 'BLU': brands.BLU_ID, 'BRIGMTON': brands.BRIGMTON_ID,
               'FACITEL': brands.FACITEL_ID, 'LG': brands.LG_ID, 'NOKIA': brands.NOKIA_ID, 'SPC': brands.SPC_ID,
               'TELEFUNKEN': brands.TELEFUNKEN_ID, 'THOMSON': brands.THOMSON_ID, 'ULEFONE': brands.ULEFONE_ID,
               'WIKO': brands.WIKO_ID}

BPs = {'FAMILY': families.BP_FAMILY_ID, 'BRANDS': __BP_BRANDS}

# SD MEMORY

__SDM_BRANDS = {'GSKILL': brands.GSKILL_ID, 'INTENSO': brands.INTENSO_ID, 'KINGSTON': brands.KINGSTON_ID,
                'SAMSUNG': brands.SAMSUNG_ID, 'SANDISK': brands.SANDISK_ID, 'TOSHIBA': brands.TOSHIBA_ID}

SDMs = {'FAMILY': families.SDM_FAMILY_ID, 'BRANDS': __SDM_BRANDS}
