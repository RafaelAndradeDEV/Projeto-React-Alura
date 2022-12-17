"""                         Aula 1
#Em geral, o React vem para nos ajudar em torno da organização do nosso código, para tal tarefa, dentro dele podemos escrever HTML e CSS juntos, dentro de um arquivo .JS

# Dentre os artifícios de organização de desenvolvimento temos: 
- A criação de tags próprias, utilizando métodos e chamando eles através de tag com seu nome
- Criação de styles para tags em específico, com a ajuda da biblioteca react que atribui uma classe específica aquela função, desta forma elementos que foram atribuidos estilo dentro da função, são os únicos a receber a atribuição.

# Estrutura clássica React:
export default function Home() {
  return (
    <div>Feliz</div>
    );
  }

Os componentes que queremos renderizar basta chamar junto a função "export default"

#  Temos que ao criar uma função e chama-lá dentro do elemento que está sendo renderizado, o que estiver dentro da tag será deixado de lado, para recebermos ela como parâmetro podemos fazer:

Ex: function Titulo (){
  return(
    <h1>Ignora qualquer coisa na tag principal</h1>
  );
}

export default Home() {
  return (
    <Titulo>Hello</Titulo>        //Chamada da função que ignora o "Hello" dentro da tag
  );
}

//Para ajustar:

function Titulo (props){
  return(
    <h1>{props.children}</h1>         //dentro de chaves, dessa forma o que estiver dentro será tratado como   
  );                                  //valor dinâmico do JS 
}

export default Home() {
  return (
    <Titulo>Hello</Titulo>        //Chamada da função que aceita o que está dentro como parâmetro
  );
}

Colocando Style dentro de um componente:

function Titulo (props){
  return(
  <>                                          //Para uso de css dentro é necessário somente um elemento pai
    <h1>{props.children}</h1>
    <style jsx>{`                             // dentro de chaves e (`` - shift + acento agudo) 
      h1 {
        color: red;
      }
    `}</style>
  </>
  );                                  
}

export default Home() {
  return (
    <Titulo tag="h2">Hello</Titulo>           //Todo atributo dentro do elemento chamado, vira props para uso
  );
}

utilizando atributos em elementos:




function Title(props) {
  const Tag = props.tag || 'h1';            //Pega o que foi atribuído, para então usar
  return (
    <>
      <Tag>{props.children}</Tag>           //Pode ter qualquer atribuição(h2,div,h1...)
      <style jsx>{`                         
      ${Tag} {                              //Utilizando a Const Tag para atribuir estilo para ela
        color: ${appConfig.theme.colors.neutrals["200"]}
        font-size: 24px;
        font-weight: 600;
      }
    `}</style>
    </>
  );
}

export default Home() {
  return (
    <Titulo tag="h2">Hello</Titulo>           //Todo atributo dentro do elemento chamado, vira props para uso
  );
}

Fazendo estilo global:

function GlobalStyle(){
  return(
    <style global jsx>{`
      * {
        background-color:Black;
      }
    `}</style>
  );
}

export default function Home(){
  return (
    <GlobalStyle/>
  )
}

                                    FORMAS DE TER UM CSS SEPARADO E FÁCIL DE MANUTENÇÃO

****Criando cores e variações de tonalidades delas 

#Criar um arquivo .json
#"theme": {
    "colors": {
      "primary": {
        "050": "#E3F9E5"
      }}
#Criando uma herança de nomes que podem ser preenchidos e posteriormente usados no projeto principal por meio do import:

import appConfig from "../config.json"

Para usar mesmo padrão: 
${appConfig.}   //Ir buscando por herança



***CSS IN JS

Criado um arquivo .js com o seguinte código:
export const theme = {
  colors: {
    primary: {
      500: '#EF9142',
    }
  }
}

import {theme} from '../pages/namefile'
<style jsx>{`
    h1 {
      background-color: ${theme.colors.primary[500]};  // para usar fazer busca por hierarquia
    }
  `}</style>


Importando Fonts:

No head da página:       //Utilizando o site:https://fonts.google.com/specimen/Open+Sans+Condensed
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">

Para usar basta colocar no style:
<style jsx>{`
    h1 {
      background-color: ${theme.colors.primary[500]};  // para usar fazer busca por hierarquia
      font-family: 'Open Sans Condensed', sans-serif;
    }
  `}</style>

Ou por meu de import, segue os detalhes:

import { Head } from "next/document"

function Importador() {
  return (<Head>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet" />
  </Head >
  );
}

export const Fonts = {
  OpenSans: {
    font: 'Open Sans Condensed, sans-serif',
  }
}

export const TextSize = {
  size: {
    10: '10px',
    15: '15px',
  }
}














 """
