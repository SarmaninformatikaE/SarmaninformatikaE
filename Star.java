
package javaapplication2;

public class Star {
    private String merek;
    private int harga;

    public Star(String merek, int harga) {
        this.merek = merek;
        this.harga = harga;
    }

    public String getMerek() {
        return merek;
    }

    public void setMerek(String merek) {
        this.merek = merek;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        this.harga = harga;
    }
    
}
