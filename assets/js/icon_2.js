const setFavicon = () => {
    const favicon = document.querySelector('link[rel="icon"]');
    favicon.href = (window.matchMedia('(prefers-color-scheme: dark)').matches)
                    ? '../../assets/drawable/logo_dark.svg'
                    : '../../assets/drawable/logo_light.svg';
};

window.matchMedia('(prefers-color-scheme: dark)')
      .addEventListener('change', setFavicon)

setFavicon()
