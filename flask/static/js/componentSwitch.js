
function switchOnetoTwo() {
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
    let pc_marks = document.getElementById('pc_marks').value;

    localStorage.setItem('os_marks', os_marks);
    localStorage.setItem('aoa_marks', aoa_marks);
    localStorage.setItem('se_marks', se_marks);
    localStorage.setItem('cn_marks', cn_marks);
    localStorage.setItem('es_marks', es_marks);
    localStorage.setItem('coa_marks', coa_marks);
    localStorage.setItem('math_marks', math_marks);
    localStorage.setItem('comm_marks', comm_marks);
    localStorage.setItem('pc_marks', pc_marks);

    form1.style.display = 'none';
    form2.style.display = 'inline';
}

function switchTwotoOne() {
    form1.style.display = 'inline';
    form2.style.display = 'none';
}

function switchTwotoThree() {
    let form3 = document.getElementById('form3');
    let form2 = document.getElementById('form2');

    let logic = document.getElementById('logic').value;
    let work_hours = document.getElementById('work_hours').value;
    let coding_skills = document.getElementById('coding_skills').value;
    let communication_skills = document.getElementById('communication_skills').value;

    localStorage.setItem('logic', logic);
    localStorage.setItem('work_hours', work_hours);
    localStorage.setItem('coding_skills', coding_skills);
    localStorage.setItem('communication_skills', communication_skills);

    form2.style.display = 'none';
    form3.style.display = 'inline';
}

function switchThreetoTwo() {
    let form2 = document.getElementById('form2');
    let form3 = document.getElementById('form3');

    form2.style.display = 'inline';
    form3.style.display = 'none';
}

function switchThreetoFour() {
    let form3 = document.getElementById('form3');
    let form4 = document.getElementById('form4');

    if (document.getElementById('long_hours_yes').checked) {
        localStorage.setItem('long_hours', 'yes');
    }

    if (document.getElementById('self_learner_yes').checked) {
        localStorage.setItem('self_learner', 'yes');
    }

    if (document.getElementById('extra_curricular_yes').checked) {
        localStorage.setItem('extra_curricular', 'yes');
    }

    form3.style.display = 'none';
    form4.style.display = 'inline';
}

function switchFourtoThree() {
    form3.style.display = 'inline';
    form4.style.display = 'none';
}

function switchFourToFive() {
    let form4 = document.getElementById('form4');
    let form5 = document.getElementById('form5');

    let cert_arr = [];
    let workshops_arr = [];
    for (let i = 1; i < 10; i++) {
        let ids = "cert" + i;
        if (document.getElementById(ids).checked) {
            cert_arr.push(document.getElementById(('cert' + i)).value);
        }
    }

    for (let i = 1; i < 9; i++) {
        let ids = "workshop" + i;
        if (document.getElementById(ids).checked) {
            workshops_arr.push(document.getElementById(('workshop' + i)).value);
        }
    }

    localStorage.setItem('certificates', cert_arr);
    localStorage.setItem('workshops', workshops_arr);

    form4.style.display = 'none';
    form5.style.display = 'inline';
}

function switchFiveToSix() {
    let form5 = document.getElementById('form5');
    let form6 = document.getElementById('form6');

    let read_write = "poor";
    let memory = "poor";

    if (document.getElementById('read-write-excellent').checked) {
        read_write = "excellent";
    } else if (document.getElementById('read-write-medium').checked) {
        read_write = "medium";
    } else {
        read_write = "poor";
    }

    if (document.getElementById('memory-excellent').checked) {
        memory = "excellent";
    } else if (document.getElementById('memory-medium').checked) {
        memory = "medium";
    } else {
        memory = "poor";
    }

    localStorage.setItem('memory', memory);
    localStorage.setItem('read_write', read_write);

    form5.style.display = 'none';
    form6.style.display = 'inline';
}

function switchSixToSeven() {
    let form6 = document.getElementById('form6');
    let form7 = document.getElementById('form7');

    let interests_arr = [];
    let career_interests_arr = [];

    for (let i = 1; i < 9; i++) {
        var ids = "interests" + i;
        if (document.getElementById(ids).checked) {
            interests_arr.push(document.getElementById(ids).value);
        }
    }

    for (let i = 1; i < 7; i++) {
        var ids = "career_interest" + i;
        if (document.getElementById(ids).checked) {
            career_interests_arr.push(document.getElementById(ids).value);
        }
    }

    let future_plans;

    if (document.getElementById('job').checked) {
        future_plans = "job";
    } else {
        future_plans = "higherstudies";
    }

    //interests = subject interests in this one
    localStorage.setItem('interests', interests_arr);
    localStorage.setItem('career_interests', career_interests_arr);
    localStorage.setItem('future_plans', future_plans);


    form6.style.display = 'none';
    form7.style.display = 'inline';
}
function switchSevenToEight() {
    let form7 = document.getElementById('form7');
    let form8 = document.getElementById('form8');

    let company_pref_arr = [];
    for (let i = 0; i < 9; i++) {
        let ids = "company_choice" + i;
        if (document.getElementById(ids).checked) {
            company_pref_arr.push(document.getElementById(ids).value);
        }
    }

    localStorage.setItem('company_pref', company_pref_arr);

    form7.style.display = 'none';
    form8.style.display = 'inline';
}
function switchEightToNine() {
    let form8 = document.getElementById('form8');
    let form9 = document.getElementById('form9');

    form8.style.display = 'none';
    form9.style.display = 'inline';
}

function eight() {
    if (document.getElementById('manage_tech_choice1').checked) {
        localStorage.setItem('management_choice', 'management');
    } else {
        localStorage.setItem('management_choice', 'technical');
    }

    if (document.getElementById('team_before_yes').checked) {
        localStorage.setItem('team_before', 'yes');
    } else {
        localStorage.setItem('team_before', 'no');
    }

    if (document.getElementById('work_sal1').checked) {
        localStorage.setItem('work_salary', 'salary');
    } else {
        localStorage.setItem('work_salary', 'satisfaction');
    }

    if (document.getElementById('hard_smart1').checked) {
        localStorage.setItem('hard_smart', 'hard');
    } else {
        localStorage.setItem('hard_smart', 'smart');
    }

    if (document.getElementById('introvert_not2').checked) {
        localStorage.setItem('introvert_not', 'no');
    } else {
        localStorage.setItem('introvert_not', 'yes');
    }

    submit_form();
}

function submit_form(){
    let data = localStorage

    console.log(data)

    fetch('/form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
}