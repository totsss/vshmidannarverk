%for i in data["result"]:
    %if name = i("company"):


        <h3>fyrirtæki : {{i['strCompanyMi']}}</h3>
        <h3>staðsetning : {{i['name']}}</h3>
        <h3>bensin95 : {{i['dblCompanyMin']}}</h3>
        <h3>diesel : {{i['diesel']}}</h3>

