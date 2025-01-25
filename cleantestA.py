class DataHandler:
    def run(self, data_list):
        # 간단한 데이터 가공
        processed_data = []
        for item in data_list:
            processed_data.append(item * 2)

        # 가공된 데이터 출력
        print("Processed data: ", processed_data)

        # 파일로 저장
        file = open("result.txt", "w")
        for d in processed_data:
            file.write(str(d) + "\n")
        file.close()

        # 데이터 길이에 따라 추가 작업
        if len(processed_data) > 5:
            print("Data size is quite large.")

        return processed_data