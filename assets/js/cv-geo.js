(function () {
  const FRENCH_COUNTRIES = new Set([
    'FR','BE','CH','LU','MC','CA',
    'SN','CI','ML','BF','NE','TD','CM','GA','CG','CD',
    'MG','BJ','TG','GN','RW','BI','DJ','KM','MU','MR',
    'SC','HT','GP','MQ','GF','RE','YT','PF','NC','PM','WF','MF','VU'
  ]);

  function applyGeoCv(isFrench) {
    document.querySelectorAll('.cv-link').forEach(function (link) {
      var path = isFrench ? link.dataset.cvFr : link.dataset.cvEn;
      if (path) link.href = path;
    });
  }

  var cached = sessionStorage.getItem('geo_cv');
  if (cached !== null) {
    applyGeoCv(cached === 'fr');
    return;
  }

  fetch('https://ipapi.co/country_code/')
    .then(function (r) { return r.text(); })
    .then(function (code) {
      var isFrench = FRENCH_COUNTRIES.has(code.trim().toUpperCase());
      sessionStorage.setItem('geo_cv', isFrench ? 'fr' : 'en');
      applyGeoCv(isFrench);
    })
    .catch(function () {
      applyGeoCv(false);
    });
})();
