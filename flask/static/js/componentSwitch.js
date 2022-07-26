function switchOnetoTwo(){
    let form1 = document.getElementById('form1');
    let form2 = document.getElementById('form2');

    let os_marks = document.getElementById('os_marks').value;
    let aoa_marks = document.getElementById('aoa_marks').value;
    let se_marks = document.getElementById('se_marks').value;
    let cn_marks = document.getElementById('cn_marks').value;
    let es_marks = document.getElementById('es_marks').value;
    let coa_marks = document.getElementById('coa_marks').value;
    let math_marks = document.getElementById('math_marks').value;
    let comm_marks = document.getElementById('comm_marks').value;

    localStorage.setItem('os_marks',os_marks);
    localStorage.setItem('aoa_marks',aoa_marks);
    localStorage.setItem('se_marks',se_marks);
    localStorage.setItem('cn_marks',cn_marks);
    localStorage.setItem('es_marks',es_marks);
    localStorage.setItem('coa_marks',coa_marks);
    localStorage.setItem('math_marks', math_marks);
    localStorage.setItem('comm_marks', comm_marks);
    
    form1.style.display = 'none';
    form2.style.display = 'inline';
}

function switchTwotoOne(){
    form1.style.display = 'inline';
    form2.style.display = 'none';
}

function switchTwotoThree(){
    let form3 = document.getElementById('form3');
    let form2 = document.getElementById('form2');

    let logic = document.getElementById('logic').value; 
    let work_hours = document.getElementById('work_hours').value;
    let coding_skills = document.getElementById('coding_skills').value;
    let communication_skills = document.getElementById('communication_skills').value;

    localStorage.setItem('logic',logic);
    localStorage.setItem('work_hours',work_hours);
    localStorage.setItem('coding_skills',coding_skills);
    localStorage.setItem('communication_skills',communication_skills);

    form2.style.display = 'none';
    form3.style.display = 'inline';
}

function switchThreetoTwo(){
    let form2 = document.getElementById('form2');
    let form3 = document.getElementById('form3');

    form2.style.display = 'inline';
    form3.style.display = 'none';
}
function switchFourToFive(){
    let form4 = document.getElementById('form4');
    let form5 = document.getElementById('form5');

    form4.style.display = 'none';
    form5.style.display = 'inline';
}
function switchFiveToSix(){
    let form5 = document.getElementById('form5');
    let form6 = document.getElementById('form6');

    form5.style.display = 'none';
    form6.style.display = 'inline';
}
function switchSixToSeven(){
    let form6 = document.getElementById('form6');
    let form7 = document.getElementById('form7');

    form6.style.display = 'none';
    form7.style.display = 'inline';
}
function switchSevenToEight(){
    let form7 = document.getElementById('form7');
    let form8 = document.getElementById('form8');

    form7.style.display = 'none';
    form8.style.display = 'inline';
}
function switchEightToNine(){
    let form8 = document.getElementById('form8');
    let form9 = document.getElementById('form9');

    form8.style.display = 'none';
    form9.style.display = 'inline';
}

