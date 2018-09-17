import brands
import families

# Motherboards

__MB_BRANDS = {'ASROCK': brands.ASROCK_ID, 'ASUS': brands.ASUS_ID, 'GIGABYTE': brands.GIGABYTE_ID, 'MSI': brands.MSI_ID}

MBs = {'FAMILY': families.MB_FAMILY_ID, 'BRANDS': __MB_BRANDS}

# CPU

__CPU_BRANDS = {'AMD': brands.AMD_ID, 'INTEL': brands.INTEL_ID}

CPUs = {'FAMILY': families.CPU_FAMILY_ID, 'BRANDS': __CPU_BRANDS}

# HDD

__HDD_BRANDS = {'APACER': brands.APACER_ID, 'CORSAIR': brands.CORSAIR_ID, 'CRUCIAL': brands.CRUCIAL_ID,
                'HP': brands.HP_ID, 'INTEL': brands.INTEL_ID, 'INTENSO': brands.INTENSO_ID,
                'KINGSTON': brands.KINGSTON_ID, 'LACIE': brands.LACIE_ID, 'MAXTOR': brands.MAXTOR_ID,
                'SAMSUNG': brands.SAMSUNG_ID, 'SANDISK': brands.SANDISK_ID, 'SEAGATE': brands.SEAGATE_ID,
                'TOSHIBA': brands.TOSHIBA_ID, 'TRANSCEND': brands.TRANSCEND_ID,
                'WESTERN_DIGITAL': brands.WESTERN_DIGITAL_ID}

HDDs = {'FAMILY': families.HDD_FAMILY_ID, 'BRANDS': __HDD_BRANDS}

# GPU

__GPU_BRANDS = {'ASUS': brands.ASUS_ID, 'EVGA': brands.EVGA_ID, 'GIGABYTE': brands.GIGABYTE_ID,
                'MSI': brands.MSI_ID, 'OEM': brands.OEM_ID, 'PALIT': brands.PALIT_ID, 'PNY': brands.PNY_ID,
                'POINT_OF_VIEW': brands.POINT_OF_VIEW_ID, 'SAPPHIRE': brands.SAPPHIRE_ID, 'ZOTAC': brands.ZOTAC_ID}

GPUs = {'FAMILY': families.GPU_FAMILY_ID, 'BRANDS': __GPU_BRANDS}

# RAM

__RAM_BRANDS = {'A_DATA': brands.A_DATA_ID, 'CORSAIR': brands.CORSAIR_ID, 'CRUCIAL': brands.CRUCIAL_ID,
                'GSKILL': brands.GSKILL_ID, 'KINGSTON': brands.KINGSTON_ID, 'MUSHKIN': brands.MUSHKIN_ID,
                'TRANSCEND': brands.TRANSCEND_ID, 'V7': brands.V7_ID}

RAMs = {'FAMILY': families.RAM_FAMILY_ID, 'BRANDS': __GPU_BRANDS}

# OPTICAL DRIVE UNITS

__ODU_BRANDS = {'ASUS': brands.ASUS_ID, 'LG': brands.LG_ID, 'LITEON': brands.LITEON_ID}

ODUs = {'FAMILY': families.ODU_FAMILY_ID, 'BRANDS': __ODU_BRANDS}

# CARD READER

__CR_BRANDS = {'CONCEPTRONIC': brands.CONCEPTRONIC_ID, 'KINGSTON': brands.KINGSTON_ID, 'NGS': brands.NGS_ID,
               'SATECHI': brands.SATECHI_ID, 'TACENS': brands.TACENS_ID, 'TOOQ': brands.TOOQ_ID,
               'TRUST': brands.TRUST_ID, 'UNOTEC': brands.UNOTEC_ID, 'WOXTER': brands.WOXTER_ID}

CRs = {'FAMILY': families.CR_FAMILY_ID, 'BRANDS': __CR_BRANDS}

# SOUND CARDS

__SC_BRANDS = {'APPROX': brands.APPROX_ID, 'ASUS': brands.ASUS_ID, 'CREATIVE': brands.CREATIVE_ID,
               'HYPERX': brands.HYPERX_ID, 'OEM': brands.OEM_ID, 'STARTECH': brands.STARTECH_ID,
               'TACENS': brands.TACENS_ID, 'UNOTEC': brands.UNOTEC_ID}

SCs = {'FAMILY': families.SC_FAMILY_ID, 'BRANDS': __SC_BRANDS}

# PC BOXES

__PCB_BRANDS = {'AEROCOOL': brands.AEROCOOL_ID, 'ANTEC': brands.ANTEC_ID, 'BMOVE': brands.BMOVE_ID,
                'BULTACO': brands.BULTACO_ID, 'COOLER_MASTER': brands.COOLER_MASTER_ID, 'CORSAIR': brands.CORSAIR_ID,
                'ENERMAX': brands.ENERMAX_ID, 'EVGA': brands.EVGA_ID, 'FRACTAL': brands.FRACTAL_ID,
                'GIGABYTE': brands.GIGABYTE_ID, 'INTEL': brands.INTEL_ID, 'LLINK': brands.LLINK_ID,
                'NFORTEC': brands.NFORTEC_ID, 'NOX': brands.NOX_ID, 'NZXT': brands.NZXT_ID,
                'OWLOTECH': brands.OWLOTECH_ID, 'PHANTEKS': brands.PHANTEKS_ID, 'SHARKOON': brands.SHARKOON_ID,
                'SILVERSTONE': brands.SILVERSTONE_ID, 'TACENS': brands.TACENS_ID, 'THERMALTAKE': brands.THERMALTAKE_ID,
                'TOOQ': brands.TOOQ_ID}

PCBs = {'FAMILY': families.PCB_FAMILY_ID, 'BRANDS': __PCB_BRANDS}

# PC BOXES ACCESSORIES

__PCBA_BRANDS = {'AEROCOOL': brands.AEROCOOL_ID, 'APPROX': brands.APPROX_ID, 'CORSAIR': brands.CORSAIR_ID,
                 'FELLOWES': brands.FELLOWES_ID, 'NZXT': brands.NZXT_ID, 'OEM': brands.OEM_ID,
                 'PCCABLENET': brands.PCCABLENET_ID, 'PHANTEKS': brands.PHANTEKS_ID,
                 'SILVERSTONE': brands.SILVERSTONE_ID,
                 'THERMALTAKE': brands.THERMALTAKE_ID}

PCBAs = {'FAMILY': families.PCBA_FAMILY_ID, 'BRANDS': __PCBA_BRANDS}

# BAREBONES

__BB_BRANDS = {'ASUS': brands.ASUS_ID, 'GIGABYTE': brands.GIGABYTE_ID, 'INTEL': brands.INTEL_ID, 'MSI': brands.MSI_ID,
               'ZOTAC': brands.ZOTAC_ID}

BBs = {'FAMILY': families.BB_FAMILY_ID, 'BRANDS': __BB_BRANDS}

# COOLERS

__C_BRANDS = {'ANTEC': brands.ANTEC_ID, 'ARTIC': brands.ARTIC_ID, 'ARTIC_SILVER': brands.ARTIC_SILVER_ID,
              'COOLER_MASTER': brands.COOLER_MASTER_ID, 'COOLTEK': brands.COOLTEK_ID, 'CORSAIR': brands.CORSAIR_ID,
              'EKWB': brands.EKWB_ID, 'ENERMAX': brands.ENERMAX_ID, 'FRACTAL': brands.FRACTAL_ID,
              'GSKILL': brands.GSKILL_ID, 'NANOXIA': brands.NANOXIA_ID, 'NOCTUA': brands.NOCTUA_ID,
              'NOX': brands.NOX_ID,
              'NZXT': brands.NZXT_ID, 'OEM': brands.OEM_ID, 'PHANTEKS': brands.PHANTEKS_ID,
              'SILVERSTONE': brands.SILVERSTONE_ID, 'TACENS': brands.TACENS_ID,
              'THERMAL_GRIZZLY': brands.THERMAL_GRIZZLY_ID, 'THERMALTAKE': brands.THERMALTAKE_ID}

Cs = {'FAMILY': families.C_FAMILY_ID, 'BRANDS': __C_BRANDS}

# POWER SUPPLY

__PS_BRANDS = {'AEROCOOL': brands.AEROCOOL_ID, 'ANTEC': brands.ANTEC_ID, 'COOLER_MASTER': brands.COOLER_MASTER_ID,
               'CORSAIR': brands.CORSAIR_ID, 'ENERMAX': brands.ENERMAX_ID, 'EVGA': brands.EVGA_ID,
               'FRACTAL': brands.FRACTAL_ID, 'LLINK': brands.LLINK_ID, 'NFORTEC': brands.NFORTEC_ID,
               'NOX': brands.NOX_ID,
               'NZXT': brands.NZXT_ID, 'OWLOTECH': brands.OWLOTECH_ID, 'PHOENIX': brands.PHOENIX_ID,
               'SEASONIC': brands.SEASONIC_ID, 'SHARKOON': brands.SHARKOON_ID, 'SILVERSTONE': brands.SILVERSTONE_ID,
               'TACENS': brands.TACENS_ID, 'THERMALTAKE': brands.THERMALTAKE_ID, 'TOOQ': brands.TOOQ_ID,
               'TPLINK': brands.TPLINK_ID}

PSs = {'FAMILY': families.PS_FAMILY_ID, 'BRANDS': __PS_BRANDS}

# MODDING

__M_BRANDS = {'CABLEMOD': brands.CABLEMOD_ID, 'COOLTEK': brands.COOLTEK_ID, 'CORSAIR': brands.CORSAIR_ID,
              'NANOXIA': brands.NANOXIA_ID, 'NZXT': brands.NZXT_ID, 'OEM': brands.OEM_ID,
              'PHANTEKS': brands.PHANTEKS_ID,
              'SILVERSTONE': brands.SILVERSTONE_ID, 'THERMALTAKE': brands.THERMALTAKE_ID}

Ms = {'FAMILY': families.M_FAMILY_ID, 'BRANDS': __M_BRANDS}

# VIDEO EDITING

__VE_BRANDS = {'AVERMEDIA': brands.AVERMEDIA_ID, 'ELGATO': brands.ELGATO_ID, 'UNOTEC': brands.UNOTEC_ID,
               'WOXTER': brands.WOXTER_ID}

VEs = {'FAMILY': families.VE_FAMILY_ID, 'BRANDS': __VE_BRANDS}

# PC WIRES

__PCW_BRANDS = {'CABLEMOD': brands.CABLEMOD_ID, 'DIGITUS': brands.DIGITUS_ID, 'NANOCABLE': brands.NANOCABLE_ID,
                'OEM': brands.OEM_ID, 'OWLOTECH': brands.OWLOTECH_ID, 'PCCABLENET': brands.PCCABLENET_ID,
                'PHANTEKS': brands.PHANTEKS_ID, 'SILVERSTONE': brands.SILVERSTONE_ID, 'STARTECH': brands.STARTECH_ID,
                'THERMALTAKE': brands.THERMALTAKE_ID}

PCWs = {'FAMILY': families.PCW_FAMILY_ID, 'BRANDS': __PCW_BRANDS}

# CONNECTIVITY

__CN_BRANDS = {'APPLE': brands.APPLE_ID, 'APPROX': brands.APPROX_ID, 'ASUS': brands.ASUS_ID, 'BELKIN': brands.BELKIN_ID,
               'BLUESTORK': brands.BLUESTORK_ID, 'CONCEPTRONIC': brands.CONCEPTRONIC_ID, 'EQUIP': brands.EQUIP_ID,
               'GENERICA': brands.GENERICA_ID, 'HP': brands.HP_ID, 'KENSINGTON': brands.KENSINGTON_ID,
               'LLINK': brands.LLINK_ID, 'LINKSYS': brands.LINKSYS_ID, 'MINIX': brands.MINIX_ID,
               'MOBVOI': brands.MOBVOI_ID, 'NGS': brands.NGS_ID, 'NZXT': brands.NZXT_ID, 'OEM': brands.OEM_ID,
               'ONE_FOR_ALL': brands.ONE_FOR_ALL_ID, 'OWLOTECH': brands.OWLOTECH_ID, 'PCCABLENET': brands.PCCABLENET_ID,
               'PHOENIX': brands.PHOENIX_ID, 'SATECHI': brands.SATECHI_ID, 'SILVERSTONE': brands.SILVERSTONE_ID,
               'STARTECH': brands.STARTECH_ID, 'TPLINK': brands.TPLINK_ID, 'TRANSCEND': brands.TRANSCEND_ID,
               'TRENDNET': brands.TRENDNET_ID, 'TRUST': brands.TRUST_ID, 'UNOTEC': brands.UNOTEC_ID,
               'XIAOMI': brands.XIAOMI_ID}

CNs = {'FAMILY': families.CN_FAMILY_ID, 'BRANDS': __CN_BRANDS}
