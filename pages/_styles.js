import { Head } from "next/document"

export const theme = {
  colors: {
    primary: {
      500: '#EF9142',
    }
  }
}

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
