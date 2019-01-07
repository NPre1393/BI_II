proc_ord = ['389', '392', '395', '398', '401', '404', '407', '410', '413', '416', '419', '422', '425', '428', '431', '434', '437', '440', '443', '446', '449', '452', '455', '458', '461', '464', '467', '470', '473', '476', '479', '482', '485', '488', '491', '494', '497', '500', '503', '506', '509', '512', '515', '518', '521', '524', '527', '530', '533', '536', '539', '542', '545', '548', '551', '554', '557', '561', '564', '567', '570', '573', '576', '579', '607', '610', '613', '616', '619', '622', '625', '628', '631', '634', '637', '640', '643', '646', '649', '652', '655', '658', '661', '664', '667', '670', '673', '676', '679', '682', '685', '688', '691', '694', '697', '700', '703', '706', '709', '712', '715', '718', '721', '725', '728', '731', '734', '737', '740', '743', '746', '749', '752', '755', '758', '761', '764', '767', '770', '773', '776', '779', '782', '785', '788', '791', '794', '797', '800', '803', '806', '809', '812', '815', '818', '821', '824', '827', '830', '833', '836', '839','842', '845', '848', '851', '854', '857', '860', '863', '866', '869', '872', '875', '878', '881', '884', '887', '890', '893', '896', '899', '902', '905', '908', '911', '914', '917', '920', '923', '929', '932', '935', '938', '941', '944', '947', '950', '953', '956', '959', '962', '965', '968', '971', '974', '977', '980', '983', '986', '989', '992', '995', '998', '1001', '1004', '1007', '1010', '1013', '1016', '1019', '1022', '1025']
order_counter = len(proc_ord)
proc = {512: 513, 1025: 1026, 515: 516, 518: 519, 521: 522, 524: 525, 527: 528, 530: 531, 533: 534, 536: 537, 539: 540, 542: 543, 545: 546, 548: 549, 551: 552, 554: 555, 557: 558, 561: 562, 564: 565, 567: 568, 570: 571, 573: 574, 576: 577, 579: 580, 607: 608, 610: 611, 613: 614, 616: 617, 619: 620, 622: 623, 625: 626, 628: 629, 631: 632, 634: 635, 637: 638, 640: 641, 643: 644, 646: 647, 649: 650, 652: 653, 655: 656, 658: 659, 661: 662, 664: 665, 667: 668, 670: 671, 673: 674, 676: 677, 679: 680, 682:683, 685: 686, 688: 689, 691: 692, 694: 695, 697: 698, 700: 701, 703: 704, 706: 707, 709: 710, 712: 713, 715: 716, 718: 719, 721: 723, 725: 726, 728: 729, 731: 732, 734: 735, 737: 738, 740: 741, 743: 744, 746: 747, 749: 750, 752: 753, 755: 756, 758: 759, 761: 762, 764: 765, 767: 768, 770: 771, 773: 774, 776: 777, 779: 780, 782: 783, 785: 786, 788: 789, 791: 792, 794: 795, 797: 798, 800: 801, 803: 804, 806: 807, 809: 810, 812: 813, 815: 816, 818: 819, 821: 822, 824: 825, 827: 828, 830: 831, 833: 834, 836: 837, 839: 840, 842: 843, 845: 846, 848: 849, 851: 852, 854: 855, 857: 858, 860: 861, 863: 864, 866: 867, 869: 870, 872: 873, 875: 876, 878: 879, 881: 882, 884: 885, 887: 888, 890: 891, 893: 894, 896: 897, 386: 387, 899: 900, 389: 390, 902: 903, 392: 393, 905: 906, 395: 396, 908: 909, 398: 399, 911: 912, 401: 402, 914:915, 404: 405, 917: 918, 407: 408, 920: 921, 410: 411, 923: 924, 413: 414, 926: 927, 416: 417, 929: 930, 419: 420, 932: 933, 422: 423, 935: 936, 425: 426, 938: 939, 428: 429, 941: 942, 431: 432, 944: 945, 434: 435, 947: 948, 437: 438, 950: 951, 440: 441, 953: 954, 443: 444, 956: 957, 446: 447, 959: 960, 449: 450, 962: 963, 452: 453, 965: 966, 455: 456, 968: 969, 458: 459, 971: 972, 461: 462, 974: 975, 464: 465, 977: 978, 467: 468, 980: 981, 470: 471, 983: 984, 473: 474, 986: 987, 476: 477, 989: 990, 479: 480, 992: 993, 482: 483, 995: 996, 485: 486, 998: 999, 488: 489, 1001: 1002, 491: 492, 1004: 1005, 494: 495, 1007: 1008, 497: 498, 1010: 1011, 500: 501, 1013: 1014, 503: 504, 1016: 1017, 506: 507, 1019: 1020, 509: 510, 1022: 1023}
proc_counter = 0
mach = {513: 514, 1026: 1027, 516: 517, 519: 520, 522: 523, 525: 526, 528: 529, 531: 532, 534: 535, 537: 538, 540: 541, 543: 544, 546: 547, 549: 550, 552: 553, 555: 556, 558: 559, 562: 563, 565: 566, 568: 569, 571: 572, 574: 575, 577: 578, 580: 581, 608: 609, 611: 612, 614: 615, 617: 618, 620: 621, 623: 624, 626: 627, 629: 630, 632: 633, 635: 636, 638: 639, 641: 642, 644: 645, 647: 648, 650: 651, 653: 654, 656: 657, 659: 660, 662: 663, 665: 666, 668: 669, 671: 672, 674: 675, 677: 678, 680: 681, 683:684, 686: 687, 689: 690, 692: 693, 695: 696, 698: 699, 701: 702, 704: 705, 707: 708, 710: 711, 713: 714, 716: 717, 719: 720, 723: 724, 726: 727, 729: 730, 732: 733, 735: 736, 738: 739, 741: 742, 744: 745, 747: 748, 750: 751, 753: 754, 756: 757, 759: 760, 762: 763, 765: 766, 768: 769, 771: 772, 774: 775, 777: 778, 780: 781, 783: 784, 786: 787, 789: 790, 792: 793, 795: 796, 798: 799, 801: 802, 804: 805, 807: 808, 810: 811, 813: 814, 816: 817, 819: 820, 822: 823, 825: 826, 828: 829, 831: 832, 834: 835, 837: 838, 840: 841, 843: 844, 846: 847, 849: 850, 852: 853, 855: 856, 858: 859, 861: 862, 864: 865, 867: 868, 870: 871, 873: 874, 876: 877, 879: 880, 882: 883, 885: 886, 888: 889, 891: 892, 894: 895, 897: 898, 387: 388, 900: 901, 390: 391, 903: 904, 393: 394, 906: 907, 396: 397, 909: 910, 399: 400, 912: 913, 402: 403, 915:916, 405: 406, 918: 919, 408: 409, 921: 922, 411: 412, 924: 925, 414: 415, 927: 928, 417: 418, 930: 931, 420: 421, 933: 934, 423: 424, 936: 937, 426: 427, 939: 940, 429: 430, 942: 943, 432: 433, 945: 946, 435: 436, 948: 949, 438: 439, 951: 952, 441: 442, 954: 955, 444: 445, 957: 958, 447: 448, 960: 961, 450: 451, 963: 964, 453: 454, 966: 967, 456: 457, 969: 970, 459: 460, 972: 973, 462: 463, 975: 976, 465: 466, 978: 979, 468: 469, 981: 982, 471: 472, 984: 985, 474: 475, 987: 988, 477: 478, 990: 991, 480: 481, 993: 994, 483: 484, 996: 997, 486: 487, 999: 1000, 489: 490, 1002: 1003, 492: 493, 1005: 1006, 495: 496, 1008: 1009, 498: 499, 1011: 1012, 501: 502,1014: 1015, 504: 505, 1017: 1018, 507: 508, 1020: 1021, 510: 511, 1023: 1024}
mach_counter = 0
#procs_orderings = []

for elem in proc_ord:
    #procs_orderings.append(int(elem))
    if int(elem) in proc:
        proc_counter +=1
        if proc[int(elem)] in mach:
            mach_counter +=1

print(order_counter, proc_counter, mach_counter)
