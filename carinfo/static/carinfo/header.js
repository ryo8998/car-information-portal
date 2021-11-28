// console.log("hoge");

// const config = {
//     carMakerSelector:document.getElementById("id_car_maker"),
//     carModelSelector:document.getElementById("id_car_model"),
//     beginYearSelector:document.getElementById("id_begin_year"),
//     endYearSelector:document.getElementById("id_end_year"),
//     beginYear:1938,
//     endYear:new Date().getFullYear(),
// }

// const CARMAKERS = 
// [{"Make_ID":440,"Make_Name":"ASTON MARTIN"},
// {"Make_ID":441,"Make_Name":"TESLA"},
// {"Make_ID":442,"Make_Name":"JAGUAR"},
// {"Make_ID":443,"Make_Name":"MASERATI"},
// {"Make_ID":444,"Make_Name":"LAND ROVER"},
// {"Make_ID":445,"Make_Name":"ROLLS ROYCE"},
// {"Make_ID":448,"Make_Name":"TOYOTA"},
// {"Make_ID":449,"Make_Name":"MERCEDES-BENZ"},
// {"Make_ID":452,"Make_Name":"BMW"},
// {"Make_ID":454,"Make_Name":"BUGATTI"}]


// CarMaker初期化
// for(let carMaker of CARMAKERS){
//     config.carMakerSelector.innerHTML +=
//     `<option value=${carMaker.Make_Name}>${carMaker.Make_Name}</option>`
// }
//beginyear endyear初期化
// for(let year=config.beginYear;year<=config.endYear;year++){
    // config.beginYearSelector.innerHTML +=`
    //     <option value="${year}">${year}</option>
    // `
//     config.endYearSelector.innerHTML +=`
//         <option value="${year}">${year}</option>
//     `
// }

// getCarModelByMaker(carMakerSelector.value);
// 選択されたCarmakerに基づき、APIから対象のモデル取得する
// config.carMakerSelector.addEventListener("change",(e)=>{
//     console.log(e.target.value);
//     getCarModelByMaker(e.target.value);
// })
// config.carMakerSelector.addEventListener("load",(e)=>{
//     console.log("wrong")
//     getCarModelByMaker(e.target.value);
// })

// todo fetchしてcarmaker選択ごとに対応するデータを取ってくるコードを実装する
// async function getCarModelByMaker(maker){
//     // let res = await fetch(`https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/${maker.toLowerCase()}?format=json`);
//     // const headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"};
//     const myHeaders = new Headers({"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"});
//     let res = await fetch(`https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getModels&make=${maker}`,{headers:myHeaders});
//     console.log(res);
//     // Todo　同一のAPIにできないかチャレンジする
//     let data = await res.json();
//     let models = data["Results"];
//     console.log(models)
//     if(models.length === 0){
//         config.carModelSelector.innerHTML = `<option value="">Car Model</option>`;
//         return
//     }
//     config.carModelSelector.innerHTML = "";
//     for(let model of models){
//         config.carModelSelector.innerHTML +=
//         `<option value=${model.Model_Name}>${model.Model_Name}</option>`
//     }
// }
