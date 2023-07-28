
document.getElementById("student").addEventListener("click", signinFunction);
document.getElementById("teacher").addEventListener("click", signinFunction);
document.getElementById("pass-student").addEventListener("keyup", signinFunction)
document.getElementById("pass-teacher").addEventListener("keyup", signinFunction)
// var csspage="";
function signinFunction(event) {
    // window.alert(event.type);
    if(event.type === "click" || (event.type === "keyup" && event.keyCode === 13)){
        const usernameStudent = document.getElementById("user-student").value;
        const passwordStudent = document.getElementById("pass-student").value;
        const usernameTeacher = document.getElementById("user-teacher").value;
        const passwordTeacher = document.getElementById("pass-teacher").value;
        if (usernameStudent === "admin-student" && passwordStudent === "admin-student") { 
            window.location.href="branchboard/student";
            // csspage="student";
        }
        else if (usernameTeacher === "admin-teacher" && passwordTeacher === "admin-teacher") {
            window.location.href="branchboard/teacher";
            // csspage="teacher";
        }
        else {
            alert("Incorrect Credentials!" );
        }
    }
    
}
