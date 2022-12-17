""""                Aula 4
Integrando com o Supabase.io. Basicamente um http.get(), para pegar o json e utilizar a informação em outro lugar

                **IMPORTANTE OLHAR DOCUMENTAÇÃO DO SUPABASE SOBRE SEGURANÇA**

fetch("https://api.github.com/users/peas")    //Método para pegar URL de algum local, demora um pouco 
.then( async (respostaDoServidor) => {        //para processar, por isso colocamos, que após ele pegar
    const respostaEsperada = await respostaDoServidor.json();   // transformar as strings em um documento
    console.log(respostaEsperada)}    //json, porque são todos em pedaços. Usamos também wait e async para 
)                                     //o processamento posterior a transformação


import { createClient } from '@supabase/supabase-js';

const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTY0MzkzMzYxNSwiZXhwIjoxOTU5NTA5NjE1fQ.4C6UujtKTFxTadz9cZstZaQQlfuHf6UU74VDHqzE4C0'
const SUPABASE_URL = 'https://dkuazfruoxylhqwrnuoi.supabase.co'
const supabaseCliente = createClient(SUPABASE_URL, SUPABASE_ANON_KEY)

#Fazemos a utilização da biblioteca do supabase, conseguimos encurtar em muito nosso caminho para conseguir um acesso rápido, de outra forma("Fetch") demoria mais.

supabaseCliente
  .from('mensagens')
  .select('*')
  .then((dados) => {
    console.log("Dados da consulta", dados)
  });

#Esse script acima ele é um efeito colateral, quando chega um dado externo, ele executa, para diminuirmos o fluxo de utilização padrão usamos um método do React



**

    supabaseClient
      .from('mensagens')  //Tabela
      .insert([
        // Tem que ser um objeto com os mesmos campos que você escreveu no supabase
        mensagem        //colunas(texto, de, id não precisa porque é uma primary key)
      ])
      .then(({ data }) => {     
        console.log('Criando mensagem: ', data)
        setListaDeMensagens([
          data[0],            //A mensagem quando digita, recebe a posição 0 do array
          ...listaDeMensagens,   //carrega o restante das mensagens
        ]);
      })

    setMensagem('rafael');
  }



React.useEffect(() => {         //Ele roda sempre que a página carrega, e os casos são descritos no "[]"
    supabaseClient
      .from('mensagens')
      .select('*')
      .order('id', { ascending: false })  //Organizar de acordo com a numeração em decrescente
      .then(({ data }) => {               //Poderia ser organizado também pela váriavel de tempo
        console.log("Dados da consulta", data)
        setListaDeMensagens(data);
      });
  }, [])   //Essas são os triggers de acionamento da função, se colocar "mensagem", sempre que houver mudança na mensagem, acionará esse método. Muito cuidado pois ela se for colocada Listademensagens, inicia um loop





"""
