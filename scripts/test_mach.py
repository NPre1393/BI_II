import pandas as pd
import datetime as dt
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import task3_mach as t3
from datetime import datetime
from utils.extract_features import extract_ts_features
import csv

mpl.rcParams['timezone'] = 'Europe/Vienna'

def get_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp)

def get_datetime_string(timestamp):
    return get_datetime(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def df_get_datetime(df):
    dts = []
    for item in df:
        dts.append(get_datetime(item))    
    return dts

def writeToFile(fname, df):
    with open(fname, 'a') as file:
        wr = csv.writer(file)
        wr.writerow(df)

def get_df(machs, window=3):
    df = pd.DataFrame(machs)
    df.columns = ['value', 'timestamp']
    df.value = df.value.astype(float)
    x = [dt.datetime.strptime(elem, '%Y-%m-%dT%H:%M:%S.%f') for elem in df.timestamp]
    u = [dt.datetime.timestamp(elem) for elem in x]
    df.index = df_get_datetime(u)
    df.timestamp = u
    return df
    #print(df)
    #res = df.drop('timestamp', axis=1)
    #paa_data = res.rolling(window).mean().dropna()[::window]
    #df['timestamp'] = u
    
    
def create_paa_plot(res, paa, window):
    """
    plots x-coords of interpolated dataframe and paa dataframe 
    :input res: resampled/interpolated dataframe
    :input paa: paa dataframe
    """
    #TODO: plot x,y,z,total infeatures one figure

    original_data = res.valuefeatures
    paa_data = np.array(paa.vafeatureslue)
    
    original_len = len(original_data)
    a = 0
    if not original_len % window == 0:
        a = 1
    
    print(len(original_data))
    print(len(paa_data))
    plt.plot(figsize=(12,8))
    plt.plot(np.arange(original_len), original_data, 'o-', label='Original')
    plt.plot(np.arange(window // 2,
                   (original_len + window // 2),
                   window)-a, paa_data.T, 'o--', label='PAA')
    plt.vlines(np.arange(0, original_len, window),
           original_data.min(), original_data.max(), color='g', linestyles='--', linewidth=0.5)
    plt.legend(loc='best', fontsize=14)
    plt.show()
"""
#fName = "1363058b-e88a-4ce4-8ef0-92f3197046df.xes.yaml"
#fName = "596ae4e1-ddc6-4f7c-b85b-45e31db907e0.xes.yaml"
#fName = "9cd024b9-dba2-4676-bec7-fde13f294cf6.xes.yaml"

#fName = "ccf8b5f9-45e6-4b52-aa65-7cdd555eca05.xes.yaml"
#information = "State/actToolRadius"
information = ["Axis/X/aaLoad","Axis/Y/aaLoad", "Axis/Z/aaLoad"]
#machining, queue = t3.query_main(open("/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/{0}".format(fName), "r"), information)
#information = "State/actToolLength1"
fName = "ccf8b5f9-45e6-4b52-aa65-7cdd555eca05.xes.yaml"
machining2, queue2 = t3.query_main(open("/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/{0}".format(fName), "r"), information)
#print(machining)
print(machining2.keys())
#print(queue2)
#mach_ts = pd.read_csv("machining_times_c.csv", sep=";", header=0)
"""
"""
(fig, ax) = plt.subplots(1,1)
ax.plot(get_df(machining2).value)
plt.gca().set_title('Spindle/driveLoad qr 124')
#plt.savefig("img/load/Axis_Z_aaLoad_581.png")
plt.show()
"""



root_dir = "/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/"
#col_names = ['mean', 'std', 'min', '20%', '40%', '50%', '60%', '80%', 'max', 'median', 'acfmean', 'acfstd', 'acfmedian', 'qstatmean', 'qstatstd', 'qstatmedian', 'mda', 'max_index', 'sma_sim', 'sma_adv', 'sma_sim_abs', 'sma_adv_abs', 'energy', 'iqr', 'entropy', 'autoreg_coeff', 'kurtosis', 'skewness', 'length', 'trace_id', 'qr']
#col_names = ['Axis/X/aaLoad_mean', 'Axis/X/aaLoad_std', 'Axis/X/aaLoad_min', 'Axis/X/aaLoad_20%', 'Axis/X/aaLoad_40%', 'Axis/X/aaLoad_50%', 'Axis/X/aaLoad_60%', 'Axis/X/aaLoad_80%', 'Axis/X/aaLoad_max', 'Axis/X/aaLoad_median', 'Axis/X/aaLoad_acfmean', 'Axis/X/aaLoad_acfstd', 'Axis/X/aaLoad_acfmedian', 'Axis/X/aaLoad_qstatmean', 'Axis/X/aaLoad_qstatstd', 'Axis/X/aaLoad_qstatmedian', 'Axis/X/aaLoad_mda', 'Axis/X/aaLoad_max_index', 'Axis/X/aaLoad_sma_sim', 'Axis/X/aaLoad_sma_adv', 'Axis/X/aaLoad_sma_sim_abs', 'Axis/X/aaLoad_sma_adv_abs', 'Axis/X/aaLoad_energy', 'Axis/X/aaLoad_iqr', 'Axis/X/aaLoad_entropy', 'Axis/X/aaLoad_autoreg_coeff', 'Axis/X/aaLoad_kurtosis', 'Axis/X/aaLoad_skewness', 'Axis/X/aaLoad_length', 'Axis/Y/aaLoad_mean', 'Axis/Y/aaLoad_std', 'Axis/Y/aaLoad_min', 'Axis/Y/aaLoad_20%', 'Axis/Y/aaLoad_40%', 'Axis/Y/aaLoad_50%', 'Axis/Y/aaLoad_60%', 'Axis/Y/aaLoad_80%', 'Axis/Y/aaLoad_max', 'Axis/Y/aaLoad_median', 'Axis/Y/aaLoad_acfmean', 'Axis/Y/aaLoad_acfstd', 'Axis/Y/aaLoad_acfmedian', 'Axis/Y/aaLoad_qstatmean', 'Axis/Y/aaLoad_qstatstd', 'Axis/Y/aaLoad_qstatmedian', 'Axis/Y/aaLoad_mda', 'Axis/Y/aaLoad_max_index', 'Axis/Y/aaLoad_sma_sim', 'Axis/Y/aaLoad_sma_adv', 'Axis/Y/aaLoad_sma_sim_abs', 'Axis/Y/aaLoad_sma_adv_abs', 'Axis/Y/aaLoad_energy', 'Axis/Y/aaLoad_iqr', 'Axis/Y/aaLoad_entropy', 'Axis/Y/aaLoad_autoreg_coeff', 'Axis/Y/aaLoad_kurtosis', 'Axis/Y/aaLoad_skewness', 'Axis/Y/aaLoad_length', 'Axis/Z/aaLoad_mean', 'Axis/Z/aaLoad_std', 'Axis/Z/aaLoad_min', 'Axis/Z/aaLoad_20%', 'Axis/Z/aaLoad_40%', 'Axis/Z/aaLoad_50%', 'Axis/Z/aaLoad_60%', 'Axis/Z/aaLoad_80%', 'Axis/Z/aaLoad_max', 'Axis/Z/aaLoad_median', 'Axis/Z/aaLoad_acfmean', 'Axis/Z/aaLoad_acfstd', 'Axis/Z/aaLoad_acfmedian', 'Axis/Z/aaLoad_qstatmean', 'Axis/Z/aaLoad_qstatstd', 'Axis/Z/aaLoad_qstatmedian', 'Axis/Z/aaLoad_mda', 'Axis/Z/aaLoad_max_index', 'Axis/Z/aaLoad_sma_sim', 'Axis/Z/aaLoad_sma_adv', 'Axis/Z/aaLoad_sma_sim_abs', 'Axis/Z/aaLoad_sma_adv_abs', 'Axis/Z/aaLoad_energy', 'Axis/Z/aaLoad_iqr', 'Axis/Z/aaLoad_entropy', 'Axis/Z/aaLoad_autoreg_coeff', 'Axis/Z/aaLoad_kurtosis', 'Axis/Z/aaLoad_skewness', 'Axis/Z/aaLoad_length', 'trace_id', 'qr']
#prod_measures = "prod_measurements2.csv"
mach_ts = "data/axis_xyz_load.csv"
#writeToFile(mach_ts, col_names)
information = ["Axis/X/aaLoad","Axis/Y/aaLoad", "Axis/Z/aaLoad"]
df = pd.DataFrame()
fileList=['95edbc0e-9516-4751-a590-56029d670e67.xes.yaml', '95f92a8a-5bc6-4772-ac7e-93380e1f05ab.xes.yaml', '96764d34-2565-4881-b63a-8477833853a3.xes.yaml', '977886a9-1105-4222-8161-044a274e9cba.xes.yaml', '97a43247-75ef-4ea3-9258-7a17ef871808.xes.yaml', '9845acbf-8007-4bb9-a60e-ac98df34a489.xes.yaml', '98ec964d-6fd4-4a68-8dfd-262a907029a4.xes.yaml', '99bf8fb3-dee4-4726-9678-86b5b9681aec.xes.yaml', '99e9d182-0c0e-4350-a757-1c43787490a3.xes.yaml', '9a5ea89e-7d3d-4d5d-beac-3b6bbe251f8b.xes.yaml', '9c155862-cc89-4be3-8eba-36c67c301ece.xes.yaml', '9cd024b9-dba2-4676-bec7-fde13f294cf6.xes.yaml', '9d91e9ac-3c03-4415-8ff7-536cfd16b07f.xes.yaml', '9d9a799e-d85f-4564-9f09-b386f02873d9.xes.yaml', '9de04815-6873-4e30-991a-32549dfed207.xes.yaml', '9e98d59e-24cb-4058-be70-cf753eef21d6.xes.yaml', '9ed23846-4bca-4dba-9a9c-0cf9696ed446.xes.yaml', '9eedeb7f-c157-4bbb-92f5-294ac7163fde.xes.yaml', '9f010e97-b02c-4873-bbd1-dd5db5b05b07.xes.yaml', '9f1e56ec-a7e5-4ffe-9061-a0e6f566277e.xes.yaml', '9f31b924-d846-4a56-a586-43ab667535bf.xes.yaml', '9f6f35e0-b7e2-4e93-9dca-40bf7d90314b.xes.yaml', '9f70db3d-132f-491a-b228-88d81f7ba9a5.xes.yaml', 'a018888d-979d-4d7e-a70b-0c2ca47b8227.xes.yaml', 'a02d2755-898f-405e-adc9-fb6400167e2d.xes.yaml', 'a16812c2-5af9-4e50-bf65-04cc2f5ad89f.xes.yaml', 'a1e8595d-6159-4eb8-b732-cc5d39f3c1a4.xes.yaml', 'a2847fdd-49b3-467e-9e8c-dd4213ac6fb1.xes.yaml', 'a32b35ec-ad91-44ee-adea-5c7996091167.xes.yaml', 'a425537b-c779-4a8b-be19-2e1be2dba1c0.xes.yaml', 'a502d234-0a2f-481b-89dc-3bdb381a4e91.xes.yaml', 'a51bf1af-d0e0-4012-839d-40d633646fde.xes.yaml', 'a5693a9e-781f-4818-be74-cf796fbb790a.xes.yaml', 'a5715360-ba22-4e16-b45e-304f68561be8.xes.yaml', 'a59cd967-bf96-4637-aa97-7244e893a2f0.xes.yaml', 'a66c2b37-e21f-4edd-92f9-fb79114c902f.xes.yaml', 'a6acd2a0-70cf-43a3-806d-8d74a4b0add0.xes.yaml', 'a6dcc33f-ac3a-4691-824a-5b94ee4c813d.xes.yaml', 'a72443f2-1342-4786-86b9-76722531e81b.xes.yaml', 'a86f9776-5ae2-4396-81b7-7fe73fee5432.xes.yaml', 'a8aa0506-83a5-48db-a4e0-e63adf7b2890.xes.yaml', 'a8ec83e3-d54a-4cc2-a3f3-fb60ab4648c9.xes.yaml', 'aa0eae5a-6727-49fd-8486-646541da4a18.xes.yaml', 'aaa8dabb-ed45-4ac1-bd0a-4a48697e54ff.xes.yaml', 'aab259cd-e0b8-4562-82f9-d3efbca6b0dd.xes.yaml', 'ab637f0d-8f83-4326-a103-5ae0a40eddb3.xes.yaml', 'ac2184fe-fe25-4c44-9cce-1f03bfcb3cae.xes.yaml', 'aca8882a-c443-42d7-9744-ac23e80a6e9c.xes.yaml', 'ad42a311-ad3f-43c2-8068-f2b57ce1a2e8.xes.yaml', '78f8e73e-9566-4ed9-a765-584b43317f08.xes.yaml', '7ddde29e-e1dd-4cc2-a863-485000d4061d.xes.yaml', '805d431e-14cd-4493-9aec-bd3e957a4c31.xes.yaml', '86fc1b57-6618-49a8-be66-ea98d446a940.xes.yaml', '8c168744-03fb-492c-b8ba-eb419a2cef1f.xes.yaml', '8fbbc868-ec27-4fd4-975f-fd67f82295f3.xes.yaml', '93215b62-36a9-40e7-b48c-5fbda2539dd9.xes.yaml', '9836ffe7-b907-492d-8635-cd873af2ddad.xes.yaml', '9eb179a4-e3b7-41d3-b752-02b112ab169e.xes.yaml', 'a1f29c8b-4f95-4ff8-a6ee-78b4c84b279b.xes.yaml', '3d6d1c07-f219-4d00-a420-8f8b8d28a515.xes.yaml', '72c62a82-0723-438a-af34-a1d605ff7297.xes.yaml', 'a70102e4-1e45-447f-9105-153982fd006f.xes.yaml', 'add21a21-a457-43b9-8a8a-c464e2b1e0ee.xes.yaml', 'add50670-b4a1-48e6-b96c-317de81519b8.xes.yaml', 'adf7c8ac-a405-4ba7-98d7-b102897b8ac2.xes.yaml', 'ae2e053a-8830-4ec4-b469-dc9303cfb70b.xes.yaml', 'aea30dc2-3ec0-43d6-b6e9-5c3d95786b95.xes.yaml', 'aeb54357-4837-4d65-80f8-2119890ce2e8.xes.yaml', 'af01b057-2985-44ea-b6d9-ae3744506b74.xes.yaml', 'afa17b44-e884-41a1-b522-c0766baed860.xes.yaml', 'afe2751b-5dbd-480b-a08a-c2802ac7f81a.xes.yaml', 'b0197659-98f0-41c8-bdaa-ee7502458de4.xes.yaml', 'b02a6417-f002-4a0d-9345-ea7a9bb24dd5.xes.yaml', 'b0927bfa-11a9-4aa3-a814-fff8f2cb2e51.xes.yaml', 'b0a9c306-ce1f-4a6b-83bd-8747a2615d15.xes.yaml', 'b1af3f56-6e38-411e-a8f2-6312e65b6d49.xes.yaml', 'b1b3458e-454b-474a-8f03-40d8c177a333.xes.yaml', 'b318cb02-e135-40ec-bc3d-14a03058de8d.xes.yaml', 'b345f61e-e606-4ffa-9a9a-f7c8691d76eb.xes.yaml', 'b353b8dc-0d2f-463f-b72a-44ff5a043bed.xes.yaml', 'b37bf706-7af9-46d0-b74e-b925d98e10cd.xes.yaml', 'b391aebd-4a9c-48d0-b954-0a45dd8f32e0.xes.yaml', 'b563bb9f-ede9-49b1-8bed-95d14653f613.xes.yaml', 'b5a177a7-6f7c-4755-a062-5c2b3b1ee43a.xes.yaml', 'b5c6f622-14b5-463c-b92e-637d5646171d.xes.yaml', 'b5c95b02-6d72-4e83-9568-7fe786861fd3.xes.yaml', 'b5f48f2e-758a-4131-a379-ab234a40f261.xes.yaml', 'b60d534c-5097-4810-b290-40b2c8b6dc89.xes.yaml', 'b7fd06bf-c578-472d-b1bb-23175e4f5049.xes.yaml','b821fdaf-411a-4d25-83ed-093118fc2414.xes.yaml', 'b83fa938-46e3-49e4-8906-427aa545cd87.xes.yaml', 'b85a7add-b56c-4aed-8d44-795c31bf1a4c.xes.yaml', 'b8ecd1c2-1b51-4c83-992b-0c2f78490b90.xes.yaml', 'b943ad88-e911-403c-816a-ae7a847b8a36.xes.yaml', 'b9888571-d7e9-47f3-b570-8cdf633a0dbd.xes.yaml', 'bb6a7999-2e85-4ba8-b662-a5e2e6029863.xes.yaml', 'bb7044f3-feed-43db-8790-b7e5f16018e7.xes.yaml', 'bb857050-4812-412b-bbce-c9b716917c9d.xes.yaml', 'bbfb8a6f-e05f-4e3f-a9bf-8fa347b823eb.xes.yaml', 'bcba2cbf-ad4b-4375-81e0-4b8b3f52128a.xes.yaml', 'bcecc53d-2081-43fc-9ec7-2968f673e823.xes.yaml', 'bd02f0ad-03fd-4a64-a041-7ec3c2410e12.xes.yaml', 'bd85945f-0907-471a-8702-29f4bd21e505.xes.yaml', 'bdbce452-9de4-4cc2-a7b5-3a7bbf275374.xes.yaml', 'bdd9e7eb-f092-4c2f-8edb-014bf077adef.xes.yaml', 'be50cdc9-fff0-4d2f-b90e-1e7f4d619079.xes.yaml', 'beea8456-dcde-486d-bf53-6c8db940e2b4.xes.yaml', 'bf0ecc92-cad1-4008-8fd3-eada17c1270a.xes.yaml', 'bf17785a-0ce2-47c3-aaa0-63665ee1488e.xes.yaml', 'bfd2794e-53bf-42f5-93a1-588d192e6614.xes.yaml', 'bfe19b3a-9155-464f-93d0-73db9d23d2a4.xes.yaml', 'bff68425-1df4-4d14-ace7-bafc28a26b3e.xes.yaml', 'c057402b-9274-43b3-a35a-3af0164b633f.xes.yaml', 'c06ca4b0-2dde-42cb-be7a-0d05f5167da7.xes.yaml', 'c0d01d5e-911f-4649-9ccb-115624539183.xes.yaml', 'c162cc05-22ae-4270-9cab-1bd7003565f6.xes.yaml', 'c2667c80-be44-4038-a2e8-d4198359e776.xes.yaml', 'c3073e33-bd83-44a1-aef0-52f9452f09e9.xes.yaml', 'c31b045b-cc87-4180-bb4c-59f7c736d27d.xes.yaml', 'c31fcd4a-a17b-49d6-aad5-0eed0728d4c5.xes.yaml', 'c3711aed-44f5-4f73-80a6-4de51ea1c72b.xes.yaml', 'c37348d5-2160-407d-b113-3dbf5816a06f.xes.yaml', 'c3951efd-9aa2-4980-8800-fe72d5be349b.xes.yaml', 'c3c07c8a-c183-431f-ab9c-1278e287bf77.xes.yaml', 'c5d5e9e1-5108-44e5-99f1-e782c6b3234a.xes.yaml', 'c71e7fae-0f7b-4a43-b01f-49062dd38f30.xes.yaml', 'c74e3d4b-d61d-4547-8faf-4e397f4ac213.xes.yaml', 'c87616cd-5720-4dee-aa56-d3b7a5c23081.xes.yaml', 'c8e22943-b751-477b-ae7c-3f405ddb1e33.xes.yaml', 'c939a6dc-9aca-469b-b3c8-0ab36fa68d8e.xes.yaml', 'c9b094eb-e89f-4377-807c-f7b30f16de1d.xes.yaml', 'cad96bb6-2396-4d14-8302-86108c2556a7.xes.yaml', 'caf2e5af-ebe5-4207-885b-f0063b26fcd1.xes.yaml', 'cb108ccf-b720-4157-93a9-59cad578579b.xes.yaml', 'cb1f3851-637b-428c-a963-ee7b898399b2.xes.yaml', 'cb8d1046-0fcf-47ab-b3a5-7c942ce0d731.xes.yaml', 'cba6a1ab-c237-41aa-a644-451a0c5a650c.xes.yaml', 'cc4be719-91b7-4e05-a30b-e2cda9b90bfb.xes.yaml', 'cc59d33f-7f94-4444-b3c8-0cc3e3c9d071.xes.yaml', 'ccf8b5f9-45e6-4b52-aa65-7cdd555eca05.xes.yaml', 'cd4c65f0-7297-47b6-84cc-0aafa3f12f03.xes.yaml', 'ce24e5ce-eee4-4a2e-88cf-7c140c23b8d2.xes.yaml', 'ced6cfa4-8415-4924-a401-a30d9797129d.xes.yaml', 'cf08013b-1ba4-4e0c-8b5c-1578318e2f14.xes.yaml', 'cf38b17a-dd51-4687-9de4-9cc3049ffdda.xes.yaml', 'cff9107a-c821-43f0-9cde-e4373228992b.xes.yaml', 'd0853e75-a95b-49e0-b094-91d37ebeebfb.xes.yaml', 'd1e79c04-d3c1-4c8c-8d88-307b2ec0fc42.xes.yaml', 'd1e80396-fdf7-47bc-bb3a-e11364ac499e.xes.yaml', 'd204b8bc-fff4-45ee-9c25-024563e27171.xes.yaml', 'd3ccc0f5-d43b-4d8c-8a42-cc9b08c8b9bd.xes.yaml', 'd4f25b6d-c8f4-4548-bc4b-146ea5494498.xes.yaml', 'd525c2aa-1564-49ce-b81a-5c71ca038d84.xes.yaml', 'd541b524-4ba1-4875-a565-43e416caf1a4.xes.yaml', 'd54f1f8f-8170-4052-b376-b154ca24e31c.xes.yaml', 'd578b87f-4685-4c74-896b-32ed660b7fb0.xes.yaml', 'd5b49811-82ab-4a8d-8992-e55c530c1988.xes.yaml', 'd611dfc1-3bc1-49b1-87ea-3abff2dbe616.xes.yaml', 'd629c2da-84f5-4349-927c-e03cc626b944.xes.yaml', 'd69e5ecb-26b6-4544-8821-670835c5eb09.xes.yaml', 'd6d1f71e-aaf9-4471-a335-a5b81e88d7ec.xes.yaml', 'd741ac52-cc94-4381-aa00-eff7bbc29df3.xes.yaml', 'd7f9b8d3-6acc-4a80-84d6-d2f0f64646cb.xes.yaml', 'd8407f4c-17f6-4e26-81e7-d91ae0596d89.xes.yaml', 'd8690c24-8374-4b13-a357-ecf36c89164c.xes.yaml', 'd88b61f7-e269-410c-aa80-317b00776793.xes.yaml', 'd8e9cbdd-3988-4f40-b9a8-ab67fa6eef35.xes.yaml', 'd8f5b0e4-e37b-4f37-859d-7ceea26181b6.xes.yaml', 'd9141b44-e372-4d4d-8c77-a3bd8d50cfdc.xes.yaml', 'd93b8a1c-c770-478e-8907-5f59458c3cf2.xes.yaml', 'da7e8ed0-8650-40c3-a357-bc0e4bd30a65.xes.yaml', 'dad4c2dd-1284-42ab-afc7-19da1c51dae6.xes.yaml', 'dc55e6b1-1103-4626-bf1d-bf4c70aef05a.xes.yaml', 'dd659c72-cefe-480c-b9ff-28ef5d63e33a.xes.yaml', 'ddd168e8-8420-47be-8a5d-252909b0d153.xes.yaml', 'de00068e-ec72-4643-8192-cca39663b554.xes.yaml', 'de004b17-5769-46c4-80d1-5a42722fd3af.xes.yaml', 'de2b5f24-4e67-42ca-8593-1bface51517a.xes.yaml', 'de2c43df-5c26-442e-a797-91b647a60c9c.xes.yaml', 'de9a5406-04f3-41cc-82eb-e3f188c5bfa4.xes.yaml', 'df241a37-5469-4b6c-b4ce-686f286667ac.xes.yaml', 'df3970fc-ed8d-452d-b084-cfef0bb9a893.xes.yaml', 'dfaa414c-84d5-4d15-a96a-9b5c6074882d.xes.yaml', 'ad4cb83a-41d2-4fdc-95f2-f3eb7d94263d.xes.yaml', 'b07bad31-b3e3-43f8-ab2c-e7f2484d0803.xes.yaml', 'b5bbe31d-59df-4ba3-abd9-5b67f5b6ae8e.xes.yaml', 'ba09e73d-858c-4e33-9d5a-86b59c79aed0.xes.yaml', 'bea04241-b7df-4384-866d-75ed148e28f8.xes.yaml', 'c2c3236a-de30-4abc-9461-ac3f958fe61a.xes.yaml', 'c893950a-fd17-4811-b571-aca8d782758c.xes.yaml', 'cc751a77-a3c0-42cf-b167-9536fcb51ce6.xes.yaml', 'd2f48607-2c44-4994-891a-c7ebd365a2e6.xes.yaml', 'd6f654e9-269f-4c94-bb7f-a8c483864d59.xes.yaml', 'db2d125c-e73b-42e3-8f44-d1d9d081b95c.xes.yaml', 'dffd9673-ed26-4206-8a95-a9f9cd6c3524.xes.yaml', 'e44e7946-9496-40c9-8a34-6a22b69c5168.xes.yaml', 'e79018c0-ae47-479a-9613-cf780790541e.xes.yaml', 'ecc9c5f0-e6ea-4bcd-a148-407616514ada.xes.yaml', 'f4211a21-5a99-4df0-a145-872921c6aa39.xes.yaml', 'f7cc1db5-42e4-46fc-82f9-d0509469c6c3.xes.yaml', 'e0156908-fe46-45d6-80fb-f33265077690.xes.yaml', 'e038c487-81bd-4964-afb0-4f04579cddbc.xes.yaml', 'e0df6ff5-90e1-4f16-a192-9ffef8ef3d8d.xes.yaml', 'e159257a-c364-43e8-a4b7-50ee14772090.xes.yaml', 'e1c87ae4-d0a4-4079-b55c-d38669983266.xes.yaml', 'e2bcd499-79fe-417f-acf2-f7972d17ec1a.xes.yaml', 'e2d91db9-7e75-41d3-a4b1-548a32f1451b.xes.yaml', 'e2f6a6b6-f3ea-462d-9f85-a4c5ffaf8b67.xes.yaml', 'e2f9768b-a2c1-4ad6-9248-c8f6718c18c7.xes.yaml', 'e3546126-1640-45ca-b24f-f4504db1bfed.xes.yaml', 'e37d5348-5747-44b2-8b71-37aede3e1cf0.xes.yaml', 'e47857c0-8b0f-4ee3-b5e1-5006e9e8da41.xes.yaml', 'e47cd933-96bb-4c7f-90e5-caa83ca9724e.xes.yaml', 'e4e9eb97-783a-4bdf-bd06-5c3bcb7d23af.xes.yaml', 'e4f351d0-d96d-43a4-9da1-7d8715963d17.xes.yaml', 'e628779d-6887-41d9-b6bd-7717ada2417d.xes.yaml', 'e67a05f6-ef6d-4ade-93da-efa9df90b6ca.xes.yaml', 'e69d43b8-9bad-40b2-a6a7-bf1219414888.xes.yaml', 'e6b092c4-f2b2-404c-be1f-2c44bb266d5d.xes.yaml', 'e7051423-ce26-48f0-b23d-0a440eb01e70.xes.yaml', 'e71e7923-15af-402b-bb8e-f1e6d9360487.xes.yaml', 'e76d5190-c5e7-4bf7-a079-5b8d4805f09f.xes.yaml', 'e7c00c09-510f-421b-b743-514be64349b5.xes.yaml', 'e9d58b37-2438-4d61-b98a-84faef452aa9.xes.yaml', 'ea093f29-985b-4227-b94d-6479fff90684.xes.yaml', 'ea2a0219-c8e9-4613-b2fc-ce422c39381b.xes.yaml', 'ea310d56-24a5-468c-beee-f2f777fda481.xes.yaml', 'ea70b209-3633-4e66-b6cf-98157638aba2.xes.yaml', 'eb2a7b6c-6498-4e7a-9502-dbbcf8b22618.xes.yaml', 'eb82a3b4-7f9b-4e65-b2ff-4c3dbe60035c.xes.yaml', 'eb9ff185-d5ac-400e-9ed1-15980a03cef7.xes.yaml', 'eba2e8fc-56b9-4805-8361-51525ebd4665.xes.yaml', 'ebc717fc-da8c-478d-b1fc-e15866d2c48d.xes.yaml', 'ed376931-ec07-45ff-a80a-2e7bc94d8043.xes.yaml', 'ed6e4b38-773d-4132-9d8d-cf34d6019634.xes.yaml', 'ed7632cf-1906-4d67-a0ac-2627f4c405fc.xes.yaml', 'edf3d6d8-168d-41cd-a688-c3ac6edb7d31.xes.yaml', 'ee268d64-6c60-4436-8e4c-7bc0c084a7b6.xes.yaml', 'f02f68da-6ee0-4c37-ad93-859db0a11f7c.xes.yaml', 'f04e9f74-dbb8-4d91-ac66-999e6911c824.xes.yaml', 'f071d0d0-332f-4106-859a-1aa279bd95bf.xes.yaml', 'f07724ec-a77a-4909-90e2-668951bfc0d4.xes.yaml','f211d8ec-9476-49aa-8f0b-3c3b72ec146a.xes.yaml', 'f3fb45c0-33fa-4488-a71f-f65c766edb00.xes.yaml', 'f4365d3b-2b7e-45e2-aeee-537cf63c6b27.xes.yaml', 'f479bacc-bda4-422f-93d3-81057f030fe8.xes.yaml', 'f4815865-376f-48a0-be49-1e92824ba610.xes.yaml', 'f60c4c23-a185-4996-a2af-13d8027059ae.xes.yaml', 'f62c488e-b083-4c69-bd9c-007fe9e69524.xes.yaml', 'f64bb3be-486b-4bb3-a84a-217694e1bb0b.xes.yaml', 'f68ddd2c-ab0e-4ec9-8879-019a2bf6027b.xes.yaml', 'f719c787-ff6b-4493-bd93-18fe4fa225f9.xes.yaml', 'f73485b1-5af8-4658-a8ed-cf69db92b766.xes.yaml', 'f75c25ee-cf0e-4261-9a14-88f8c488751a.xes.yaml', 'f78b5930-76ca-4d61-b1a0-3e7f0c1229c6.xes.yaml', 'f7dae88a-3e98-4105-95f6-4d4029804253.xes.yaml', 'f819de78-8a24-40b2-8320-17c854561d01.xes.yaml', 'f9008882-3850-481b-992a-97fc8235531f.xes.yaml', 'f9a87249-90ee-4329-8a25-6719a8055f73.xes.yaml', 'faaea817-b2a5-4367-a01b-6e65b11e4f1f.xes.yaml', 'faf56387-c0fd-4549-92d4-69068efb993f.xes.yaml', 'fb0c544f-b83c-4c98-841b-54394b02505e.xes.yaml', 'fb265407-fab8-46f8-a717-e41f9d7047e2.xes.yaml', 'fb8a1fef-aa4b-4e5c-bf36-119dad224138.xes.yaml', 'fba4d201-8093-4875-ba3b-30e3d6c49390.xes.yaml', 'fbd6e10e-6647-4811-9524-667b0ade4376.xes.yaml', 'fc396afa-a92f-411d-ac2e-1e4bb86f3fac.xes.yaml', 'fd511942-6d08-4705-894e-a7627ba29261.xes.yaml', 'fdd05c42-3b9c-4b2e-a0a3-ed986fed3b0c.xes.yaml', 'fe2e4758-f61c-4301-85a4-965068a74594.xes.yaml', 'fe4352f8-784c-424b-94ab-afa2caf32c68.xes.yaml']
for dirName, subdirList, fileList2 in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        item = open(dirName+'/'+fname, 'r')    
        machs, queue = t3.query_main(item, information)   
        if len(machs) > 0:
        #fts_names = []
            print(fname, queue)
            fts = []
            for key in information:
                if key in machs.keys():   
                    if len(machs[key]) > 0: 
                        df = get_df(machs[key])
                        features, cols = extract_ts_features(df, col='value')
                        cols.append('length')
                        features.append(len(df))
                        #ft_names = [key+'_'+s for s in cols]
                        #fts_names.extend(ft_names)
                        fts.extend(features)
            fts.extend(queue)
            #fts_names.extend(['trace_id', 'qr'])
            writeToFile(mach_ts, fts)
        """
        if len(machs)>50:
            print(len(machs), queue)
            features, cols = extract_ts_features(get_df(machs), col='value')
            features.append(len(machs))
            features.extend(queue)

            #print(features)
            writeToFile(mach_ts, features)
        elif len(machs)<50 and len(machs)>0:
            print("Machining btw 0 and 50: ",len(machs), queue)
        
        
        if len(machs) > 0:
            tmp = get_df(machs)
            tmp.to_csv(mach_ts, mode='a', header=False)
            df = df.append(tmp)
            print(len(df))
        """

"""
df_plot = df.sort_values(by='timestamp')
plt.plot(df_plot.value)
plt.show()
"""

"""
print(mach_ts)
start = [dt.datetime.strptime(elem[:23], '%Y-%m-%dT%H:%M:%S.%f') for elem in mach_ts.time_calling]
end = [dt.datetime.strptime(elem[:23], '%Y-%m-%dT%H:%M:%S.%f') for elem in mach_ts.time_done]

#u = [dt.datetime.timestamp(elem) for elem in x]

durations = []
for i in range(0,len(start)):
    dur = end[i] - start[i]
    dur_s = dur.total_seconds()
    durations.append(dur_s)

mach_ts['duration'] = durations
print(mach_ts)
mach_ts.to_csv("mach_durations.csv", index=False)
"""