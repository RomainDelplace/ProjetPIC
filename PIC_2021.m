clear all
close all
clc

x=[-0.1:0.0005:0.1];
y=[-0.1:0.0005:0.1];
z=[-0.06:0.0005:.3];%Regl orig
a=20e-3;
%Pour avoir 30? d'ouverture th?orique, la largeur du piezo doit ?tre ?gale ? 2.5 mm 
b=2e-3;
% % % b=2e-3;
d0=0.1;
gamma=2.0944

%positions des capteurs dans le rep?re

y12=d0*cos(gamma-pi/2);
z12=d0*sin(gamma-pi/2);
alpha=25*pi/180;%incidence de l'axe du r?cepteur sur celui de l'?metteur
r02=-z12+y12/tan(alpha);%distance entre ?metteur et point focal
r01=sqrt((r02+z12)^2+(y12)^2);%distance entre r?cepteur et point focal sur l'axe de l'?metteur

ell_center_y=y12/2;
ell_center_z=-z12/2;
ang_ell=acos(y12./d0);

%Caracteristiques des transducteurs
lam=1480/(1000000)
k=2*pi*1000000/1480;a0=0.01;
ka=k*a0;

        h0 = waitbar(1,['Please wait...']);

steps = length(x);

%calcul des angles que form?s entre chaque point de l'espace et les axes
%emetteur (beta2) et recepteur (betax dans le plan Oyz et betay dans le
%plan Oxz)
for i=1:length(x);
    for j=1:length(y)
        for k=1:length(z);
            
            r1y=sqrt(x(i)^2+(z(k)+z12)^2);
            r2xyz=sqrt(x(i)^2+(y(j)-y12)^2+(z(k)+z12)^2);
            r2yz=sqrt((y12)^2+(z12+r02)^2);
            pscal2=-y12*(y(j)-y12)+(z(k)+z12).*(z12+r02);
            
            beta2(i,j,k)=acos(z(k)/sqrt(x(i)^2+y(j)^2+z(k)^2));
            betax(i,j,k)=acos((-y12*(y(j)-y12)+(z(k)+z12)*(z12+r02))/(sqrt(y12^2+(z12+r02)^2)*sqrt((y(j)-y12).^2+(z(k)+z12).^2)));
            betay(i,j,k)=asin(x(i)/r1y);
            beta1(i,j,k)=acos(pscal2./(r2xyz*r2yz));
            
             
            
            
        end
    end
        waitbar(i / steps,h0)
end


    close(h0) 

 %Directivite en reception ACVP
 Db=sinc((b/lam)*sin(betax));
 Da=sinc((a/lam)*sin(betay));
 D1=(Db.*Da).^2;

% % %  %Directivity patterns if receiiver is similar to emitter in bistatic config
% % %  D1=(2*besselj(1,ka*sin(beta1))./(ka*sin(beta1))).^2;
% % %  D1(find(isnan(D1(:,:,:))))=1;% dans l'axe de l'emetteur, angle nul et sinus cardinal doit etre remplace par 1

   
 %Directivite en emission ACVP
 D2=(2*besselj(1,ka*sin(beta2))./(ka*sin(beta2))).^2;
 D2(find(isnan(D2(:,:,:))))=1;% dans l'axe de l'emetteur, angle nul et sinus cardinal doit etre remplace par 1
 
 
 %Directivite totale
 Dtot=(D1.*D2);
 DDL=10*log10((Dtot));
 
 %DDL
 %imagesc(squeeze(DDL(201,:,:)))