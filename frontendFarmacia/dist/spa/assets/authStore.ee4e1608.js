import{d as e}from"./index.7d081dc2.js";const i=e("auth",{state:()=>({isAuthenticated:localStorage.getItem("isAuthenticated")==="true",user:JSON.parse(localStorage.getItem("user"))||null}),actions:{login(t){this.isAuthenticated=!0,this.user=t,localStorage.setItem("isAuthenticated","true"),localStorage.setItem("user",JSON.stringify(t))},logout(){this.isAuthenticated=!1,this.user=null,localStorage.removeItem("isAuthenticated"),localStorage.removeItem("user")},initialize(){const t=localStorage.getItem("user");t&&(this.user=JSON.parse(t),this.isAuthenticated=!0)}}});export{i as u};
