import streamlit as st
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt


def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("This is a Portfolio Optimization Web Application")
    st.subheader("You could select any stocks leveraging the Russell 2000 indexes and create your portfolio")

    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2d/Minimum_variance_flontier_of_MPT.svg")
    st.subheader("Theory implemented: Efficient Frontier from Financial Economics ")
    st.write("This web application maximizes the expected return while minimizing the portfolio volatility/variance & standard deviation")

    stock_options = st.multiselect("Select stocks from the Russell 2000 Index",['AAN',	'AAON',	'AAT',	'AAWW',	'ABCB',	'ABG',	'ABM',	'ABR',	'ABTX',	'ABUS',	'AC',	'ACA',	'ACAD',	'ACBI',	'ACCD',	'ACCO',	'ACEL',	'ACET',	'ACIW',	'ACLS',	'ACRE',	'ACRS',	'ACTG',	'ADC',	'ADN',	'ADNT',	'ADTN',	'ADUS',	'ADV',	'ADVM',	'AEIS',	'AEL',	'AEO',	'AERI',	'AEVA',	'AFCG',	'AFIB',	'AFMD',	'AGEN',	'AGIO',	'AGLE',	'AGM',	'AGS',	'AGTI',	'AGX',	'AGYS',	'AHCO',	'AHH',	'AHT',	'AIMC',	'AIN',	'AIR',	'AIT',	'AIV',	'AJRD',	'AJX',	'AKBA',	'AKR',	'AKRO',	'AKTS',	'AKUS',	'AKYA',	'ALBO',	'ALDX',	'ALE',	'ALEC',	'ALEX',	'ALG',	'ALGS',	'ALGT',	'ALHC',	'ALKS',	'ALKT',	'ALLK',	'ALLO',	'ALPN',	'ALRM',	'ALRS',	'ALT',	'ALTA',	'ALTG',	'ALTO',	'ALTR',	'ALVR',	'ALX',	'ALXO',	'AMAL',	'AMBA',	'AMBC',	'AMC',	'AMCX',	'AMEH',	'AMK',	'AMKR',	'AMN',	'AMNB',	'AMOT',	'AMPE',	'AMPH',	'AMRC',	'AMRK',	'AMRS',	'AMRX',	'AMSC',	'AMSF',	'AMSWA',	'AMTB',	'AMTI',	'AMTX',	'AMWD',	'AMWL',	'ANAB',	'ANAT',	'ANDE',	'ANF',	'ANGN',	'ANGO',	'ANIK',	'ANIP',	'ANNX',	'AOSL',	'AOUT',	'APAM',	'APEI',	'APG',	'APLE',	'APLS',	'APLT',	'APOG',	'APPF',	'APPH',	'APPN',	'APPS',	'APR',	'APTS',	'APYX',	'AQB',	'AQUA',	'AR',	'ARAY',	'ARCB',	'ARCH',	'ARCT',	'ARDX',	'ARGO',	'ARI',	'ARKO',	'ARLO',	'ARNA',	'ARNC',	'AROC',	'AROW',	'ARQT',	'ARR',	'ARRY',	'ARTNA',	'ARVN',	'ARWR',	'ASAN',	'ASB',	'ASGN',	'ASIX',	'ASLE',	'ASO',	'ASPN',	'ASTE',	'ASXC',	'ATCX',	'ATEC',	'ATEN',	'ATER',	'ATEX',	'ATGE',	'ATHA',	'ATHX',	'ATI',	'ATKR',	'ATLC',	'ATNI',	'ATNX',	'ATOM',	'ATOS',	'ATRA',	'ATRC',	'ATRI',	'ATRO',	'ATRS',	'ATSG',	'AUB',	'AUD',	'AVA',	'AVAH',	'AVAV',	'AVD',	'AVID',	'AVIR',	'AVNS',	'AVNT',	'AVNW',	'AVO',	'AVRO',	'AVXL',	'AVYA',	'AWH',	'AWR',	'AX',	'AXDX',	'AXGN',	'AXL',	'AXNX',	'AXSM',	'AXTI',	'AZZ',	'B',	'BALY',	'BANC',	'BAND',	'BANF',	'BANR',	'BATRA',	'BATRK',	'BBBY',	'BBCP',	'BBIO',	'BBSI',	'BCAB',	'BCC',	'BCEL',	'BCO',	'BCOR',	'BCOV',	'BCPC',	'BCRX',	'BDC',	'BDN',	'BDSI',	'BDSX',	'BDTX',	'BE',	'BEAM',	'BECN',	'BEEM',	'BFC',	'BFLY',	'BFS',	'BFST',	'BGCP',	'BGFV',	'BGS',	'BH',	'BHB',	'BHE',	'BHLB',	'BHR',	'BHVN',	'BIG',	'BIGC',	'BIPC',	'BJ',	'BJRI',	'BKD',	'BKE',	'BKH',	'BKU',	'BL',	'BLBD',	'BLFS',	'BLI',	'BLKB',	'BLMN',	'BLNK',	'BLUE',	'BLX',	'BMEA',	'BMI',	'BMRC',	'BMTC',	'BNED',	'BNFT',	'BNGO',	'BNL',	'BOLT',	'BOMN',	'BOOM',	'BOOT',	'BOX',	'BPMC',	'BRBR',	'BRBS',	'BRC',	'BRKL',	'BRMK',	'BRP',	'BRSP',	'BRT',	'BRY',	'BSET',	'BSIG',	'BSRR',	'BTAI',	'BTRS',	'BTU',	'BTX',	'BUSE',	'BV',	'BVH',	'BVS',	'BW',	'BWB',	'BXC',	'BXMT',	'BY',	'BYRN',	'BYSI',	'BZH',	'CAC',	'CADE',	'CAI',	'CAKE',	'CAL',	'CALM',	'CALX',	'CAMP',	'CAR',	'CARA',	'CARE',	'CARG',	'CARS',	'CASA',	'CASH',	'CASS',	'CATC',	'CATO',	'CATY',	'CBAY',	'CBB',	'CBNK',	'CBRL',	'CBT',	'CBTX',	'CBU',	'CBZ',	'CCB',	'CCBG',	'CCCC',	'CCF',	'CCMP',	'CCNE',	'CCO',	'CCOI',	'CCRN',	'CCS',	'CCXI',	'CDAK',	'CDE',	'CDEV',	'CDLX',	'CDMO',	'CDNA',	'CDXC',	'CDXS',	'CDZI',	'CECE',	'CEIX',	'CELC',	'CELH',	'CENT',	'CENTA',	'CENX',	'CERE',	'CERS',	'CEVA',	'CFB',	'CFFN',	'CGEM',	'CHCO',	'CHCT',	'CHEF',	'CHK',	'CHRS',	'CHS',	'CHUY',	'CHX',	'CIA',	'CIM',	'CIO',	'CIR',	'CIT',	'CIVB',	'CIX',	'CLAR',	'CLBK',	'CLDR',	'CLDT',	'CLDX',	'CLFD',	'CLNE',	'CLNN',	'CLPR',	'CLPT',	'CLSK',	'CLVS',	'CLW',	'CMBM',	'CMC',	'CMCO',	'CMO',	'CMP',	'CMPR',	'CMRE',	'CMRX',	'CMTL',	'CNBKA',	'CNDT',	'CNK',	'CNMD',	'CNNE',	'CNO',	'CNOB',	'CNR',	'CNS',	'CNSL',	'CNST',	'CNTY',	'CNX',	'CNXN',	'COGT',	'COHU',	'COKE',	'COLB',	'COLL',	'CONN',	'COOP',	'CORE',	'CORT',	'COUR',	'COWN',	'CPE',	'CPF',	'CPK',	'CPLG',	'CPRX',	'CPS',	'CPSI',	'CRAI',	'CRC',	'CRDF',	'CRIS',	'CRK',	'CRMD',	'CRMT',	'CRNC',	'CRNX',	'CROX',	'CRS',	'CRSR',	'CRTX',	'CRVL',	'CSGS',	'CSII',	'CSLT',	'CSOD',	'CSPR',	'CSR',	'CSSE',	'CSTE',	'CSTL',	'CSTM',	'CSTR',	'CSV',	'CSWI',	'CTBI',	'CTLP',	'CTMX',	'CTO',	'CTOS',	'CTRE',	'CTRN',	'CTS',	'CTSO',	'CTT',	'CTXR',	'CUBI',	'CUE',	'CURI',	'CURO',	'CUTR',	'CVA',	'CVBF',	'CVCO',	'CVET',	'CVGI',	'CVGW',	'CVI',	'CVLG',	'CVLT',	'CVM',	'CWEN',	'CWH',	'CWK',	'CWST',	'CWT',	'CXP',	'CXW',	'CYH',	'CYRX',	'CYTK',	'CZNC',	'DAKT',	'DAN',	'DBD',	'DBI',	'DBRG',	'DCO',	'DCOM',	'DCPH',	'DDD',	'DDS',	'DEA',	'DEN',	'DENN',	'DFIN',	'DGICA',	'DGII',	'DHC',	'DHIL',	'DHT',	'DIN',	'DIOD',	'DJCO',	'DK',	'DLTH',	'DLX',	'DM',	'DMRC',	'DMS',	'DMTK',	'DNLI',	'DNMR',	'DNOW',	'DOC',	'DOCN',	'DOMO',	'DOOR',	'DORM',	'DRH',	'DRIO',	'DRNA',	'DRQ',	'DRRX',	'DS',	'DSGN',	'DSKE',	'DSP',	'DSPG',	'DSSI',	'DTIL',	'DVAX',	'DX',	'DXPE',	'DY',	'DYN',	'DZSI',	'EAF',	'EAR',	'EAT',	'EB',	'EBC',	'EBET',	'EBF',	'EBIX',	'EBS',	'EBSB',	'EBTC',	'ECHO',	'ECOL',	'ECOM',	'ECPG',	'EDIT',	'EEX',	'EFC',	'EFSC',	'EGAN',	'EGBN',	'EGHT',	'EGLE',	'EGP',	'EGRX',	'EHTH',	'EIG',	'EIGR',	'ELF',	'ELY',	'EME',	'EMKR',	'ENDP',	'ENR',	'ENS',	'ENSG',	'ENTA',	'ENV',	'ENVA',	'EOLS',	'EOSE',	'EPAC',	'EPAY',	'EPC',	'EPRT',	'EPZM',	'EQBK',	'EQC',	'ERII',	'ESCA',	'ESE',	'ESGC',	'ESGR',	'ESNT',	'ESPR',	'ESRT',	'ESTE',	'ETNB',	'ETRN',	'ETWO',	'EVC',	'EVER',	'EVH',	'EVI',	'EVLO',	'EVOP',	'EVRI',	'EVTC',	'EWTX',	'EXLS',	'EXPI',	'EXPO',	'EXTR',	'EYE',	'EYPT',	'EZPW',	'FARO',	'FATE',	'FBC',	'FBIO',	'FBK',	'FBMS',	'FBNC',	'FBP',	'FBRX',	'FC',	'FCBC',	'FCBP',	'FCEL',	'FCF',	'FCFS',	'FCPT',	'FDBC',	'FDMT',	'FDP',	'FELE',	'FF',	'FFBC',	'FFIC',	'FFIN',	'FFWM',	'FGEN',	'FHI',	'FHTX',	'FIBK',	'FISI',	'FIX',	'FIXX',	'FIZZ',	'FLGT',	'FLIC',	'FLL',	'FLMN',	'FLNT',	'FLOW',	'FLR',	'FLWS',	'FLXN',	'FLXS',	'FMBH',	'FMBI',	'FMNB',	'FMTX',	'FN',	'FNCH',	'FNKO',	'FNLC',	'FOA',	'FOCS',	'FOE',	'FOLD',	'FOR',	'FORA',	'FORM',	'FORR',	'FOSL',	'FOXF',	'FPI',	'FRBA',	'FRBK',	'FREE',	'FREQ',	'FRG',	'FRGI',	'FRME',	'FRO',	'FROG',	'FRPH',	'FRST',	'FRTA',	'FSBC',	'FSBW',	'FSP',	'FSR',	'FSS',	'FTCI',	'FTHM',	'FTSI',	'FUBO',	'FUL',	'FULC',	'FULT',	'FUV',	'FWRD',	'GABC',	'GAN',	'GATO',	'GATX',	'GBCI',	'GBIO',	'GBL',	'GBOX',	'GBT',	'GBX',	'GCI',	'GCMG',	'GCO',	'GCP',	'GDEN',	'GDOT',	'GDYN',	'GEF',	'GEO',	'GERN',	'GES',	'GEVO',	'GFF',	'GHC',	'GHL',	'GIC',	'GIII',	'GKOS',	'GLDD',	'GLNG',	'GLRE',	'GLSI',	'GLT',	'GMRE',	'GMS',	'GMTX',	'GNK',	'GNL',	'GNLN',	'GNOG',	'GNTY',	'GNUS',	'GNW',	'GOEV',	'GOGO',	'GOLF',	'GOOD',	'GOSS',	'GPI',	'GPMT',	'GPRE',	'GPRO',	'GPX',	'GRBK',	'GRC',	'GRPN',	'GRTS',	'GRWG',	'GSAT',	'GSBC',	'GSHD',	'GSKY',	'GT',	'GTBP',	'GTHX',	'GTLS',	'GTN',	'GTS',	'GTY',	'GTYH',	'GVA',	'GWB',	'GWRS',	'HA',	'HAE',	'HAFC',	'HALO',	'HARP',	'HASI',	'HAYN',	'HBB',	'HBCP',	'HBIO',	'HBMD',	'HBNC',	'HBT',	'HCAT',	'HCC',	'HCCI',	'HCHC',	'HCI',	'HCKT',	'HCSG',	'HEAR',	'HEES',	'HELE',	'HFFG',	'HFWA',	'HGEN',	'HGV',	'HI',	'HIBB',	'HIFS',	'HL',	'HLI',	'HLIO',	'HLIT',	'HLNE',	'HLX',	'HMHC',	'HMN',	'HMPT',	'HMST',	'HMTV',	'HNGR',	'HNI',	'HNST',	'HOFT',	'HOFV',	'HOMB',	'HOME',	'HONE',	'HOOK',	'HOPE',	'HOV',	'HOWL',	'HP',	'HPK',	'HQI',	'HQY',	'HR',	'HRI',	'HRMY',	'HRTG',	'HRTX',	'HSC',	'HSII',	'HSKA',	'HSTM',	'HT',	'HTBI',	'HTBK',	'HTH',	'HTLD',	'HTLF',	'HUBG',	'HURN',	'HVT',	'HWC',	'HWKN',	'HY',	'HYFM',	'HYLN',	'HYRE',	'HZO',	'IBCP',	'IBEX',	'IBIO',	'IBOC',	'IBP',	'IBRX',	'IBTX',	'ICAD',	'ICFI',	'ICHR',	'ICPT',	'IDCC',	'IDEX',	'IDT',	'IDYA',	'IEA',	'IESC',	'IGMS',	'IGT',	'IHC',	'IHRT',	'IIIN',	'IIIV',	'IIPR',	'IIVI',	'IKNA',	'ILPT',	'IMAX',	'IMGN',	'IMKTA',	'IMPL',	'IMUX',	'IMVT',	'IMXI',	'INBK',	'INBX',	'INDB',	'INDT',	'INFI',	'INFN',	'INFU',	'INGN',	'INN',	'INNV',	'INO',	'INOV',	'INS',	'INSG',	'INSM',	'INSP',	'INSW',	'INT',	'INVA',	'INVE',	'INZY',	'IOSP',	'IPAR',	'IPI',	'IRBT',	'IRDM',	'IRMD',	'IRT',	'IRTC',	'IRWD',	'ISBC',	'ISEE',	'ITCI',	'ITGR',	'ITI',	'ITIC',	'ITOS',	'ITRI',	'IVC',	'IVR',	'JACK',	'JBSS',	'JBT',	'JELD',	'JJSF',	'JNCE',	'JOAN',	'JOE',	'JOUT',	'JRVR',	'JYNT',	'KAI',	'KALA',	'KALU',	'KALV',	'KAMN',	'KAR',	'KBAL',	'KBH',	'KBR',	'KDMN',	'KDNY',	'KE',	'KELYA',	'KFRC',	'KFY',	'KIDS',	'KIRK',	'KLDO',	'KLIC',	'KMPH',	'KMT',	'KN',	'KNL',	'KNSA',	'KNSL',	'KNTE',	'KOD',	'KODK',	'KOP',	'KOPN',	'KOS',	'KPTI',	'KRA',	'KREF',	'KRG',	'KRNY',	'KRO',	'KRON',	'KROS',	'KRT',	'KRTX',	'KRUS',	'KRYS',	'KTB',	'KTOS',	'KURA',	'KVHI',	'KW',	'KWR',	'KYMR',	'KZR',	'LABP',	'LADR',	'LANC',	'LAND',	'LASR',	'LAUR',	'LAWS',	'LAZY',	'LBAI',	'LBC',	'LBRT',	'LC',	'LCII',	'LCTX',	'LCUT',	'LDL',	'LE',	'LEGH',	'LEU',	'LGIH',	'LGND',	'LHCG',	'LILA',	'LILAK',	'LIND',	'LIVN',	'LIVX',	'LKFN',	'LL',	'LLNW',	'LMAT',	'LMNR',	'LMNX',	'LNDC',	'LNN',	'LNTH',	'LOB',	'LOCO',	'LORL',	'LOTZ',	'LOVE',	'LPG',	'LPI',	'LPRO',	'LPSN',	'LQDT',	'LRN',	'LSCC',	'LSEA',	'LSF',	'LTC',	'LTHM',	'LTRPA',	'LUNA',	'LUNG',	'LXFR',	'LXP',	'LXRX',	'LZB',	'M',	'MAC',	'MANT',	'MARA',	'MASS',	'MATW',	'MATX',	'MAX',	'MAXR',	'MBI',	'MBII',	'MBIN',	'MBIO',	'MBUU',	'MBWM',	'MC',	'MCB',	'MCBC',	'MCBS',	'MCF',	'MCFT',	'MCRB',	'MCRI',	'MCS',	'MD',	'MDC',	'MDCA',	'MDGL',	'MDP',	'MDRX',	'MDVL',	'MDXG',	'MEC',	'MED',	'MEDP',	'MEG',	'MEI',	'MEIP',	'MESA',	'MFA',	'MG',	'MGEE',	'MGI',	'MGLN',	'MGNI',	'MGNX',	'MGPI',	'MGRC',	'MGTA',	'MGTX',	'MGY',	'MHLD',	'MHO',	'MIC',	'MILE',	'MIME',	'MIRM',	'MITK',	'MLAB',	'MLHR',	'MLI',	'MLR',	'MMAT',	'MMI',	'MMS',	'MMSI',	'MNKD',	'MNR',	'MNRL',	'MNRO',	'MNTV',	'MOD',	'MODN',	'MODV',	'MOFG',	'MORF',	'MOV',	'MP',	'MPAA',	'MPB',	'MPLN',	'MPX',	'MRC',	'MRLN',	'MRNS',	'MRSN',	'MRTN',	'MSBI',	'MSEX',	'MSGE',	'MSGN',	'MSON',	'MSTR',	'MTDR',	'MTEM',	'MTH',	'MTOR',	'MTRN',	'MTRX',	'MTSI',	'MTW',	'MTX',	'MUR',	'MUSA',	'MVBF',	'MVIS',	'MWA',	'MXL',	'MYE',	'MYGN',	'MYRG',	'NAPA',	'NARI',	'NAT',	'NATH',	'NATR',	'NAVI',	'NBEV',	'NBHC',	'NBR',	'NBTB',	'NCBS',	'NCMI',	'NDLS',	'NEO',	'NEOG',	'NESR',	'NEX',	'NEXI',	'NFBK',	'NG',	'NGM',	'NGMS',	'NGVC',	'NGVT',	'NH',	'NHC',	'NHI',	'NJR',	'NKLA',	'NKTX',	'NL',	'NLS',	'NLTX',	'NMIH',	'NMRK',	'NMTR',	'NNBR',	'NNI',	'NODK',	'NOG',	'NOTV',	'NOVA',	'NOVT',	'NP',	'NPCE',	'NPK',	'NPO',	'NPTN',	'NR',	'NRC',	'NRIM',	'NRIX',	'NSA',	'NSIT',	'NSP',	'NSSC',	'NSTG',	'NTB',	'NTCT',	'NTGR',	'NTLA',	'NTST',	'NTUS',	'NUS',	'NUVA',	'NUVB',	'NVEC',	'NVEE',	'NVRO',	'NVTA',	'NWBI',	'NWE',	'NWLI',	'NWN',	'NWPX',	'NX',	'NXGN',	'NXRT',	'NYMT',	'OAS',	'OBNK',	'OCDX',	'OCFC',	'OCGN',	'OCN',	'OCUL',	'OCX',	'ODC',	'ODP',	'OEC',	'OFC',	'OFG',	'OFIX',	'OFLX',	'OGS',	'OI',	'OII',	'OIS',	'OLMA',	'OLP',	'OM',	'OMCL',	'OMER',	'OMI',	'ONB',	'ONCR',	'ONCT',	'ONEM',	'ONEW',	'ONTF',	'ONTO',	'OOMA',	'OPCH',	'OPI',	'OPK',	'OPRT',	'OPRX',	'OPY',	'ORA',	'ORBC',	'ORC',	'ORGO',	'ORIC',	'ORMP',	'ORRF',	'OSBC',	'OSIS',	'OSPN',	'OSTK',	'OSUR',	'OSW',	'OTLK',	'OTRK',	'OTTR',	'OUST',	'OUT',	'OVV',	'OXM',	'OYST',	'PACB',	'PACK',	'PAE',	'PAHC',	'PAR',	'PARR',	'PASG',	'PATK',	'PAVM',	'PAYA',	'PBF',	'PBFS',	'PBH',	'PBI',	'PBYI',	'PCH',	'PCRX',	'PCSB',	'PCT',	'PCVX',	'PCYO',	'PD',	'PDCE',	'PDCO',	'PDFS',	'PDLI',	'PDM',	'PEB',	'PEBO',	'PETQ',	'PETS',	'PFBC',	'PFBI',	'PFC',	'PFGC',	'PFIS',	'PFS',	'PFSI',	'PGC',	'PGEN',	'PGNY',	'PGRE',	'PGTI',	'PHAT',	'PHR',	'PI',	'PING',	'PIPR',	'PJT',	'PKE',	'PKOH',	'PLAB',	'PLAY',	'PLBY',	'PLCE',	'PLM',	'PLMR',	'PLOW',	'PLPC',	'PLRX',	'PLSE',	'PLUS',	'PLXS',	'PLYM',	'PMT',	'PMVP',	'PNM',	'PNTG',	'POLY',	'POR',	'POWI',	'POWL',	'POWW',	'PPBI',	'PPTA',	'PRA',	'PRAA',	'PRAX',	'PRCH',	'PRDO',	'PRFT',	'PRG',	'PRGS',	'PRIM',	'PRK',	'PRLB',	'PRLD',	'PRMW',	'PRO',	'PROS',	'PRPL',	'PRTA',	'PRTG',	'PRTH',	'PRTK',	'PRTS',	'PRTY',	'PRVA',	'PRVB',	'PSB',	'PSMT',	'PSN',	'PSNL',	'PSTL',	'PSTX',	'PTCT',	'PTEN',	'PTGX',	'PTSI',	'PTVE',	'PUMP',	'PVAC',	'PVBC',	'PZN',	'PZZA',	'QADA',	'QCRH',	'QLYS',	'QMCO',	'QNST',	'QTNT',	'QTRX',	'QTS',	'QTWO',	'QUOT',	'RAD',	'RADI',	'RAIN',	'RAMP',	'RAPT',	'RAVN',	'RBB',	'RBBN',	'RBCAA',	'RBNC',	'RC',	'RCEL',	'RCII',	'RCKT',	'RCKY',	'RCM',	'RCUS',	'RDFN',	'RDN',	'RDNT',	'RDUS',	'REAL',	'REGI',	'REKR',	'REPL',	'REPX',	'RES',	'RETA',	'REV',	'REVG',	'REX',	'REZI',	'RFL',	'RGNX',	'RGP',	'RGR',	'RGS',	'RHP',	'RICK',	'RIDE',	'RIGL',	'RILY',	'RIOT',	'RLAY',	'RLGT',	'RLGY',	'RLI',	'RLJ',	'RLMD',	'RM',	'RMAX',	'RMBS',	'RMNI',	'RMO',	'RMR',	'RNA',	'RNST',	'ROAD',	'ROCK',	'ROG',	'ROIC',	'ROLL',	'RPAI',	'RPAY',	'RPD',	'RPHM',	'RPT',	'RRBI',	'RRC',	'RRD',	'RRGB',	'RRR',	'RSI',	'RUBY',	'RUSHA',	'RUSHB',	'RUTH',	'RVI',	'RVLV',	'RVMD',	'RVNC',	'RVP',	'RWT',	'RXDX',	'RXRX',	'RXT',	'RYAM',	'RYI',	'RYTM',	'SAFE',	'SAFM',	'SAFT',	'SAH',	'SAIA',	'SAIL',	'SANA',	'SANM',	'SASR',	'SATS',	'SAVA',	'SAVE',	'SB',	'SBCF',	'SBGI',	'SBH',	'SBRA',	'SBSI',	'SBTX',	'SCHL',	'SCHN',	'SCL',	'SCOR',	'SCS',	'SCSC',	'SCU',	'SCVL',	'SCWX',	'SDGR',	'SEAS',	'SEEL',	'SEER',	'SELB',	'SEM',	'SENEA',	'SENS',	'SESN',	'SFBS',	'SFIX',	'SFL',	'SFM',	'SFNC',	'SFST',	'SFT',	'SGC',	'SGH',	'SGMO',	'SGMS',	'SGRY',	'SGTX',	'SHAK',	'SHEN',	'SHO',	'SHOO',	'SHYF',	'SI',	'SIBN',	'SIEN',	'SIG',	'SIGA',	'SIGI',	'SILK',	'SITC',	'SITM',	'SJI',	'SJW',	'SKIN',	'SKT',	'SKY',	'SKYT',	'SKYW',	'SLAB',	'SLCA',	'SLDB',	'SLP',	'SLQT',	'SM',	'SMBC',	'SMBK',	'SMCI',	'SMED',	'SMMF',	'SMMT',	'SMP',	'SMPL',	'SMSI',	'SMTC',	'SNBR',	'SNCY',	'SNDX',	'SNEX',	'SNR',	'SNSE',	'SOI',	'SOLY',	'SONO',	'SP',	'SPFI',	'SPNE',	'SPNS',	'SPNT',	'SPPI',	'SPRB',	'SPRO',	'SPSC',	'SPT',	'SPTN',	'SPWH',	'SPWR',	'SPXC',	'SQZ',	'SR',	'SRCE',	'SRDX',	'SRG',	'SRI',	'SRNE',	'SRRK',	'SRT',	'SSB',	'SSD',	'SSP',	'SSTI',	'SSTK',	'STAA',	'STAG',	'STAR',	'STBA',	'STC',	'STEM',	'STEP',	'STFC',	'STIM',	'STKS',	'STMP',	'STNG',	'STOK',	'STON',	'STRA',	'STRL',	'STRO',	'STTK',	'STXS',	'SUM',	'SUMO',	'SUPN',	'SURF',	'SVC',	'SWAV',	'SWBI',	'SWIM',	'SWM',	'SWN',	'SWTX',	'SWX',	'SXC',	'SXI',	'SXT',	'SYBT',	'SYKE',	'SYNA',	'SYRS',	'TA',	'TACO',	'TALO',	'TALS',	'TARS',	'TAST',	'TBBK',	'TBI',	'TBIO',	'TBK',	'TBPH',	'TCBI',	'TCBK',	'TCMD',	'TCRR',	'TCS',	'TCX',	'TDS',	'TDW',	'TELL',	'TEN',	'TENB',	'TERN',	'TEX',	'TG',	'TGH',	'TGI',	'TGNA',	'TGTX',	'TH',	'THC',	'THFF',	'THR',	'THRM',	'THRY',	'THS',	'TIG',	'TIL',	'TILE',	'TIPT',	'TISI',	'TITN',	'TK',	'TLIS',	'TLMD',	'TLS',	'TLYS',	'TMCI',	'TMDX',	'TMHC',	'TMP',	'TMST',	'TNC',	'TNET',	'TNK',	'TNXP',	'TOWN',	'TPB',	'TPC',	'TPH',	'TPIC',	'TPTX',	'TR',	'TRC',	'TREE',	'TRHC',	'TRIL',	'TRMK',	'TRN',	'TRNO',	'TRNS',	'TROX',	'TRS',	'TRST',	'TRTN',	'TRTX',	'TRUP',	'TRVN',	'TSC',	'TSE',	'TSHA',	'TTCF',	'TTEC',	'TTEK',	'TTGT',	'TTI',	'TTMI',	'TUP',	'TVTX',	'TVTY',	'TWI',	'TWNK',	'TWO',	'TWOU',	'TWST',	'TXMD',	'TXRH',	'UAVS',	'UBA',	'UBSI',	'UCBI',	'UCTT',	'UE',	'UEC',	'UEIC',	'UFCS',	'UFI',	'UFPI',	'UFPT',	'UFS',	'UHT',	'UIHC',	'UIS',	'ULCC',	'ULH',	'UMBF',	'UMH',	'UNF',	'UNFI',	'UNIT',	'UPLD',	'UPWK',	'URBN',	'URG',	'URGN',	'USCR',	'USD',	'USLM',	'USM',	'USNA',	'USPH',	'USX',	'UTL',	'UTMD',	'UTZ',	'UUUU',	'UVE',	'UVSP',	'UVV',	'VALU',	'VAPO',	'VBIV',	'VBTX',	'VC',	'VCEL',	'VCRA',	'VCYT',	'VEC',	'VECO',	'VEI',	'VEL',	'VERI',	'VERU',	'VG',	'VGR',	'VHC',	'VHI',	'VIAV',	'VICR',	'VIEW',	'VINC',	'VIR',	'VIRX',	'VITL',	'VIVO',	'VKTX',	'VLDR',	'VLGEA',	'VLY',	'VMD',	'VNDA',	'VOR',	'VOXX',	'VPG',	'VRA',	'VRAY',	'VRCA',	'VREX',	'VRNS',	'VRNT',	'VRRM',	'VRS',	'VRTS',	'VRTV',	'VSEC',	'VSH',	'VSTM',	'VSTO',	'VTGN',	'VTOL',	'VUZI',	'VVI',	'VVNT',	'VXRT',	'WABC',	'WAFD',	'WASH',	'WBT',	'WCC',	'WD',	'WDFC',	'WERN',	'WETF',	'WGO',	'WHD',	'WINA',	'WING',	'WIRE',	'WK',	'WKHS',	'WLDN',	'WLFC',	'WLL',	'WMK',	'WNC',	'WOR',	'WOW',	'WRE',	'WRLD',	'WSBC',	'WSBF',	'WSC',	'WSFS',	'WSR',	'WTBA',	'WTI',	'WTS',	'WTTR',	'WVE',	'WW',	'WWW',	'XBIT',	'XENT',	'XGN',	'XHR',	'XL',	'XNCR',	'XOG',	'XOMA',	'XONE',	'XPEL',	'XPER',	'XXII',	'YELL',	'YELP',	'YEXT',	'YMAB',	'YORW',	'ZEUS',	'ZGNX',	'ZIOP',	'ZIXI',	'ZNTL',	'ZUMZ',	'ZUO',	'ZY',	'ZYXI',
    ])

    st.write("You selected", stock_options)

    stock_list_number = 0
    for stock_list_number in range(len(stock_options)):
        stock_list_number = stock_list_number+1

    st.write(stock_list_number)

    if stock_list_number>0:
        weights = np.full((1,stock_list_number),round((1/stock_list_number),2))
        weights = np.array(weights)
        st.write(weights)


    start_date = st.date_input("start date",value = date.fromisoformat('2013-01-01'))
    end_date = st.date_input(datetime.today().strftime('%Y-%m-%d'))

    df = pd.DataFrame()
    df.style.format("{:.2}")

    if stock_list_number>0:
        for stock in stock_options:
            df[stock]= web.DataReader(stock, data_source = "yahoo", start = start_date, end = end_date)['Adj Close']

        df.style.format(subset=[stock], formatter="{:.2f})")

        title = "Portfolio Adjusted Close History"
        my_stocks  = df
        st.write(df)
        st.write(my_stocks.columns.values)
        st.line_chart(my_stocks)

        returns = df.pct_change()
        st.subheader("Here shows the daily returns of your portfolio")
        st.write(returns)

        st.subheader("Here shows the annualized covariance matrix")
        covariance_matrix_annual = returns.cov()*252
        st.write(covariance_matrix_annual)

        np_array_covariance_matrix_annual = np.array(covariance_matrix_annual)


        st.subheader("Here shows the portfolio variance")
        portfolio_variance =  np.dot(weights, (np.dot(np_array_covariance_matrix_annual, weights.T)))
        st.write(portfolio_variance)

        st.subheader("Here shows the portfolio volatility which is the standard deviation")
        port_volatility = np.sqrt(portfolio_variance)
        st.write(port_volatility)


        st.subheader("Here shows the portfolio annualized returns")

        returns_mean_array = np.array(returns.mean())
        st.write(returns_mean_array)

        st.write(returns_mean_array*weights)

        portfolio_simple_annual_return = np.sum(returns_mean_array*weights)*252
        st.write(portfolio_simple_annual_return)


        st.subheader("this is portfolio variance")
        port_var_round = (np.round_(portfolio_variance,decimals=2))
        port_var_round_string = port_var_round.astype(str)
        st.write(port_var_round_string)


        percentage_volatility = (np.round_(port_volatility, decimals = 2)).astype(str)
        st.subheader("expected variance",  percentage_volatility)


        st.write(np.round_(port_volatility, decimals = 2))

        from pypfopt.efficient_frontier import EfficientFrontier
        from pypfopt import risk_models
        from pypfopt import expected_returns

        mu = expected_returns.mean_historical_return(df)
        standard_deviation = risk_models.sample_cov(df)


        #optimize for Sharpe Ratio
        efficient_frontier = EfficientFrontier(mu, standard_deviation)
        weights = efficient_frontier.max_sharpe()
        updated_weights = efficient_frontier.clean_weights()

        st.write(updated_weights)

        from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
        latest_prices = get_latest_prices(df)
        weights = updated_weights

        portfolio_amount = st.number_input("How much money is it in your portfolio", value = 80000)
        discrete_allocation = DiscreteAllocation(weights, latest_prices, total_portfolio_value = portfolio_amount)

        allocation, leftover = discrete_allocation.lp_portfolio()

        st.subheader("Number of shares you can purchase")
        st.write( allocation)

        st.subheader("Funds remaining")
        st.text(np.round(leftover,2))
        st.caption("dollars left")
