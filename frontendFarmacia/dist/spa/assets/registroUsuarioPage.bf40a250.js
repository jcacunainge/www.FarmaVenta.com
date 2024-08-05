import{aH as V,r as m,a2 as f,a3 as t,a5 as y,a7 as U,ac as i,a8 as a,B as r,aI as u,aa as w,aM as q,aN as N,a9 as g}from"./index.5b891057.js";import{Q as I}from"./QPage.3cb4d6cb.js";import{_ as R}from"./fondo.c1c33764.js";import{a as k,u as C}from"./UseNotify.5a832758.js";import{api as Q}from"./axios.03897a5b.js";const B=()=>({required:s=>!!s||"Requerido",requiredRule:s=>!!s||"Requerido",emailRule:s=>!s||/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(s)||"Email debe ser valido"});const v=n=>(q("data-v-37a35a12"),n=n(),N(),n),P={class:"row justify-center items-center"},S=v(()=>i("img",{class:"imgFondo col-md-5",src:R,alt:""},null,-1)),j={class:"col-md-7 column"},F=v(()=>i("div",{class:"text-h6 text-center q-mt-xs"},[g(" FarmaVenta "),i("br"),g('"Ventas r\xE1pidas, salud al instante" ')],-1)),T={class:"text-center",style:{margin:"3rem auto"}},$={class:"row q-gutter-md justify-center"},h={class:"q-gutter-md q-mt-md"},D={__name:"registroUsuarioPage",setup(n){k();const{messageWarning:p}=C(),{required:_}=B();m({required:d=>_(d)});const s=m(!0),l=m({nombre_usuario:"",codigo_usuario:"",nombre_negocio:"",dirrecion_negocio:"",telefono_negocio:"",contrase\u00F1a:"",correo:""}),b=y(),x=async()=>{var e,o;const d=JSON.stringify(l.value);try{console.log(d),await Q.post("usuario/register",d),b.push({name:"login"})}catch(c){console.log(c),p((o=(e=c==null?void 0:c.response)==null?void 0:e.data)==null?void 0:o.message)}};return(d,e)=>(U(),f(I,{class:"flex flex-center"},{default:t(()=>[i("div",P,[S,i("div",j,[F,i("div",T,[i("div",$,[a(u,{color:"blue-12",modelValue:l.value.nombre_usuario,"onUpdate:modelValue":e[0]||(e[0]=o=>l.value.nombre_usuario=o),label:"Nombre Usuario:",outlined:"",type:"text",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-user"})]),_:1},8,["modelValue"]),a(u,{color:"blue-12",modelValue:l.value.codigo_usuario,"onUpdate:modelValue":e[1]||(e[1]=o=>l.value.codigo_usuario=o),label:"Codigo Usuario:",outlined:"",type:"text",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-address-card"})]),_:1},8,["modelValue"]),a(u,{color:"blue-12",modelValue:l.value.nombre_negocio,"onUpdate:modelValue":e[2]||(e[2]=o=>l.value.nombre_negocio=o),label:"Nombre Negocio:",outlined:"",type:"text",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-home"})]),_:1},8,["modelValue"]),a(u,{color:"blue-12",modelValue:l.value.dirrecion_negocio,"onUpdate:modelValue":e[3]||(e[3]=o=>l.value.dirrecion_negocio=o),label:"Dirreci\xF3n Negocio:",outlined:"",type:"text",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-map-marker"})]),_:1},8,["modelValue"]),a(u,{color:"blue-12",modelValue:l.value.telefono_negocio,"onUpdate:modelValue":e[4]||(e[4]=o=>l.value.telefono_negocio=o),label:"Telefono Negocio:",outlined:"",type:"text",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-phone-alt"})]),_:1},8,["modelValue"]),a(u,{color:"blue-12",modelValue:l.value.correo,"onUpdate:modelValue":e[5]||(e[5]=o=>l.value.correo=o),label:"Correo:",outlined:"",type:"email",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"email"})]),_:1},8,["modelValue"]),a(u,{modelValue:l.value.contrase\u00F1a,"onUpdate:modelValue":e[7]||(e[7]=o=>l.value.contrase\u00F1a=o),label:"Contrase\xF1a",outlined:"",type:s.value?"password":"text",color:"blue-12",class:"col-xs-12 col-sm-8 col-md-8"},{prepend:t(()=>[a(r,{name:"las la-lock"})]),append:t(()=>[a(r,{name:s.value?"visibility_off":"visibility",class:"cursor-pointer",onClick:e[6]||(e[6]=o=>s.value=!s.value)},null,8,["name"])]),_:1},8,["modelValue","type"])]),i("div",h,[a(w,{type:"submit",onClick:x,label:"Iniciar Sesi\xF3n",color:"primary",style:{width:"180px"},flat:""})])])])])]),_:1}))}};var W=V(D,[["__scopeId","data-v-37a35a12"]]);export{W as default};