package com.example.econom_main.Product.dtos;
import com.fasterxml.jackson.annotation.JsonProperty;


import lombok.Data;
@Data
public class CostDto {
    public Item item;
    public Offers offers;
    @Data
    public static class Item {
        private String name;
        private String description;
        private String volume;
        private Images images;
        @Data
        public static class Images {
            private String mini_url;
            private String original_url;
            private String preview_url;
            private String product_url;
            private String small_url;
        }
    }

    @Data
    public static class Offers {
        private double lenta;
        @JsonProperty("5ka")
        private double _5ka;
        private double magnit;
        private double metro;
        private double perekrestok;
        private double auchan;
    }
}
